# 测试输入输出示例

## 测试输入示例
文件：`skills/pubmed-search/assets/test_input.json`

```json
{
  "keywords": "HPV integration clonality expression",
  "start_date": "2022/01/01",
  "end_date": "2026/12/31",
  "retmax": 5,
  "has_abstract_only": true,
  "article_types": ["journal article"]
}
```

## 对应命令
```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration clonality expression" \
  --start-date 2022/01/01 \
  --end-date 2026/12/31 \
  --retmax 5 \
  --has-abstract-only \
  --article-types "journal article" \
  --output-prefix results/pubmed_search/test_run
```

## 输出示例
- Markdown：`results/pubmed_search/test_run.md`
- CSV：`results/pubmed_search/test_run.csv`

字段包含：
- PMID
- 英文标题
- 中文标题
- 发表日期
- 期刊名
- PubMed链接
- 英文摘要
- 中文摘要

当无摘要时，对应字段为 `无摘要`。
