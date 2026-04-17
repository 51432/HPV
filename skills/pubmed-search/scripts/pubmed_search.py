#!/usr/bin/env python3
"""PubMed literature search skill script.

Modules:
1) Search (ESearch)
2) Fetch details (EFetch)
3) Translate EN->ZH
4) Export Markdown + CSV
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
USER_AGENT = "hpv-pubmed-skill/1.0"

JOURNAL_FILTER = ' OR '.join(
    [
        '"Annals Of Oncology"[Journal]',
        '"Nature"[Journal]',
        '"Cancer Cell"[Journal]',
        '"Cell"[Journal]',
        '"Science"[Journal]',
        '"Nat Genet"[Journal]',
        '"Cancer Discov"[Journal]',
        '"Cell Res"[Journal]',
        '"Mol Cancer"[Journal]',
        '"Nat Med"[Journal]',
        '"Nat Cancer"[Journal]',
        '"Cancer Commun"[Journal]',
        '"Nature Communications"[Journal]',
        '"Nat Commun"[Journal]',
    ]
)


@dataclass
class Article:
    pmid: str
    title_en: str
    title_zh: str
    pub_date: str
    journal: str
    pubmed_url: str
    abstract_en: str
    abstract_zh: str


def http_get_json(url: str, params: Dict[str, str], timeout: int = 30) -> Dict:
    full_url = f"{url}?{urlencode(params)}"
    req = Request(full_url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def http_get_text(url: str, params: Dict[str, str], timeout: int = 30) -> str:
    full_url = f"{url}?{urlencode(params)}"
    req = Request(full_url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return resp.read().decode("utf-8")


# -------------------------
# Module 1: Search
# -------------------------
def build_query(
    keywords: str,
    start_date: str,
    end_date: str,
    has_abstract_only: bool,
    article_types: Optional[List[str]],
) -> str:
    date_clause = f'("{start_date}"[Date - Publication] : "{end_date}"[Date - Publication])'
    journal_clause = f"({JOURNAL_FILTER})"
    keyword_clause = f"({keywords})"

    filters = [keyword_clause, date_clause, journal_clause]
    if has_abstract_only:
        filters.append("hasabstract[text]")

    if article_types:
        type_clause = " OR ".join([f'"{t}"[Publication Type]' for t in article_types])
        filters.append(f"({type_clause})")

    return " AND ".join(filters)


def search_pubmed(query: str, retmax: int, timeout: int = 30) -> List[str]:
    url = f"{EUTILS_BASE}/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(retmax),
        "retmode": "json",
        "sort": "pub+date",
    }
    data = http_get_json(url, params=params, timeout=timeout)
    try:
        return data["esearchresult"]["idlist"]
    except KeyError as e:
        raise RuntimeError(f"Unexpected ESearch response: missing key {e}") from e


# -------------------------
# Module 2: Fetch details
# -------------------------
def _extract_pub_date(pub_date_node: Optional[ET.Element]) -> str:
    if pub_date_node is None:
        return "Unknown"

    year = (pub_date_node.findtext("Year") or "").strip()
    month = (pub_date_node.findtext("Month") or "").strip()
    day = (pub_date_node.findtext("Day") or "").strip()
    medline_date = (pub_date_node.findtext("MedlineDate") or "").strip()

    if medline_date:
        return medline_date

    parts = [p for p in [year, month, day] if p]
    return "-".join(parts) if parts else "Unknown"


def _clean_text(text: str) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_article_details(pmids: List[str], timeout: int = 30) -> List[Dict[str, str]]:
    if not pmids:
        return []

    url = f"{EUTILS_BASE}/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }

    xml_text = http_get_text(url, params=params, timeout=timeout)
    root = ET.fromstring(xml_text)
    records: List[Dict[str, str]] = []

    for article in root.findall(".//PubmedArticle"):
        pmid = _clean_text(article.findtext(".//PMID") or "")
        title = _clean_text(article.findtext(".//ArticleTitle") or "")
        journal = _clean_text(article.findtext(".//Journal/Title") or "")

        pub_date_node = article.find(".//JournalIssue/PubDate")
        pub_date = _extract_pub_date(pub_date_node)

        abstract_texts = []
        for abs_node in article.findall(".//Abstract/AbstractText"):
            label = abs_node.attrib.get("Label")
            content = _clean_text("".join(abs_node.itertext()))
            if content:
                abstract_texts.append(f"{label}: {content}" if label else content)

        abstract = "\n".join(abstract_texts).strip() if abstract_texts else "无摘要"
        records.append(
            {
                "pmid": pmid,
                "title_en": title,
                "pub_date": pub_date,
                "journal": journal,
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                "abstract_en": abstract,
            }
        )

    order_map = {p: i for i, p in enumerate(pmids)}
    records.sort(key=lambda x: order_map.get(x["pmid"], 999999))
    return records


# -------------------------
# Module 3: Translation
# -------------------------
def translate_text_mymemory(text: str, timeout: int = 20) -> str:
    if not text or text == "无摘要":
        return "无摘要"

    url = "https://api.mymemory.translated.net/get"
    params = {"q": text[:4000], "langpair": "en|zh-CN"}
    try:
        payload = http_get_json(url, params=params, timeout=timeout)
        translated = (payload.get("responseData") or {}).get("translatedText", "").strip()
        return translated if translated else f"[翻译失败] {text}"
    except Exception as exc:  # noqa: BLE001
        logging.warning("Translation failed: %s", exc)
        return f"[翻译失败] {text}"


def translate_records(records: List[Dict[str, str]], translate_engine: str = "mymemory") -> List[Article]:
    translated: List[Article] = []
    for rec in records:
        if translate_engine == "none":
            title_zh = rec["title_en"]
            abstract_zh = rec["abstract_en"]
        else:
            title_zh = translate_text_mymemory(rec["title_en"])
            abstract_zh = translate_text_mymemory(rec["abstract_en"])
            time.sleep(0.2)

        translated.append(
            Article(
                pmid=rec["pmid"],
                title_en=rec["title_en"],
                title_zh=title_zh,
                pub_date=rec["pub_date"],
                journal=rec["journal"],
                pubmed_url=rec["pubmed_url"],
                abstract_en=rec["abstract_en"],
                abstract_zh=abstract_zh,
            )
        )
    return translated


# -------------------------
# Module 4: Output
# -------------------------
def write_csv(articles: List[Article], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "PMID",
                "英文标题",
                "中文标题",
                "发表日期",
                "期刊名",
                "PubMed链接",
                "英文摘要",
                "中文摘要",
            ]
        )
        for a in articles:
            writer.writerow([a.pmid, a.title_en, a.title_zh, a.pub_date, a.journal, a.pubmed_url, a.abstract_en, a.abstract_zh])


def write_markdown(articles: List[Article], out_md: Path) -> None:
    out_md.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "| PMID | 英文标题 | 中文标题 | 发表日期 | 期刊名 | PubMed链接 | 英文摘要 | 中文摘要 |\n"
        "|---|---|---|---|---|---|---|---|\n"
    )

    def esc(s: str) -> str:
        return (s or "").replace("|", "\\|").replace("\n", "<br>")

    rows = []
    for a in articles:
        rows.append(
            "| {pmid} | {title_en} | {title_zh} | {pub_date} | {journal} | [链接]({url}) | {abs_en} | {abs_zh} |".format(
                pmid=esc(a.pmid),
                title_en=esc(a.title_en),
                title_zh=esc(a.title_zh),
                pub_date=esc(a.pub_date),
                journal=esc(a.journal),
                url=esc(a.pubmed_url),
                abs_en=esc(a.abstract_en),
                abs_zh=esc(a.abstract_zh),
            )
        )

    out_md.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")


def valid_date(date_str: str) -> str:
    try:
        dt.datetime.strptime(date_str, "%Y/%m/%d")
        return date_str
    except ValueError as e:
        raise argparse.ArgumentTypeError("日期格式必须为 YYYY/MM/DD") from e


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PubMed 检索并导出中英文结果")
    parser.add_argument("--keywords", required=True, help="检索关键词（PubMed query）")
    parser.add_argument("--start-date", required=True, type=valid_date, help="起始日期 YYYY/MM/DD")
    parser.add_argument("--end-date", required=True, type=valid_date, help="结束日期 YYYY/MM/DD")
    parser.add_argument("--retmax", type=int, default=20, help="返回篇数上限，默认 20")
    parser.add_argument("--has-abstract-only", action="store_true", help="仅保留有摘要文章")
    parser.add_argument("--article-types", nargs="*", default=None, help='文章类型筛选，例如 review clinical trial "journal article"')
    parser.add_argument("--translate-engine", choices=["mymemory", "none"], default="mymemory", help="翻译方式")
    parser.add_argument("--output-prefix", default="results/pubmed_search/pubmed_search", help="输出文件前缀")
    return parser.parse_args()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    args = parse_args()

    try:
        query = build_query(
            keywords=args.keywords,
            start_date=args.start_date,
            end_date=args.end_date,
            has_abstract_only=args.has_abstract_only,
            article_types=args.article_types,
        )
        logging.info("PubMed query: %s", query)

        pmids = search_pubmed(query, retmax=args.retmax)
        logging.info("Found %d PMIDs", len(pmids))

        records = fetch_article_details(pmids)
        articles = translate_records(records, translate_engine=args.translate_engine)

        out_prefix = Path(args.output_prefix)
        out_csv = out_prefix.with_suffix(".csv")
        out_md = out_prefix.with_suffix(".md")

        write_csv(articles, out_csv)
        write_markdown(articles, out_md)

        logging.info("Wrote CSV: %s", out_csv)
        logging.info("Wrote Markdown: %s", out_md)
        return 0
    except Exception as e:  # noqa: BLE001
        logging.exception("Unexpected error: %s", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
