---
name: pubmed-search
description: 使用 PubMed 官方 E-utilities 进行结构化文献检索并导出中英文结果。用于需要按关键词、时间范围、摘要筛选、文章类型筛选来批量获取 PMID、标题、日期、期刊、PubMed 链接和摘要，并输出 Markdown/CSV 到 results/pubmed_search/ 的场景。
---

# PubMed Search Skill

按以下流程执行：
1. 组装 PubMed 查询语句（关键词 + 日期 + 期刊限定 + 可选过滤）。
2. 调用 ESearch 获取 PMID 列表。
3. 调用 EFetch 获取标题、日期、期刊、摘要。
4. 翻译英文标题和英文摘要为中文。
5. 输出 Markdown 表格与 CSV 到 `results/pubmed_search/`。

## 固定期刊范围
检索语句固定包含以下期刊（可在脚本中维护）：
- Annals Of Oncology
- Nature
- Cancer Cell
- Cell
- Science
- Nat Genet
- Cancer Discov
- Cell Res
- Mol Cancer
- Nat Med
- Nat Cancer
- Cancer Commun
- Nature Communications / Nat Commun

## 脚本位置
- `skills/pubmed-search/scripts/pubmed_search.py`

## 参数说明
- `--keywords`：关键词（必填）
- `--start-date`：起始日期（必填，`YYYY/MM/DD`）
- `--end-date`：结束日期（必填，`YYYY/MM/DD`）
- `--retmax`：返回上限（默认 `20`）
- `--has-abstract-only`：仅保留有摘要文章（可选）
- `--article-types`：文章类型（可选，多值），如 `review` `clinical trial` `journal article`
- `--translate-engine`：翻译方式（`mymemory` 或 `none`）
- `--output-prefix`：输出前缀（默认 `results/pubmed_search/pubmed_search`）

## 输出字段
- PMID
- 英文标题
- 中文标题
- 发表日期
- 期刊名
- PubMed链接
- 英文摘要
- 中文摘要

## 无摘要处理
若某文献无摘要，保留记录并在英文摘要/中文摘要字段写入 `无摘要`。

## 示例命令与测试样例
- 示例命令：见 `skills/pubmed-search/references/example_commands.md`
- 测试输入输出样例：见 `skills/pubmed-search/references/test_io_examples.md`
