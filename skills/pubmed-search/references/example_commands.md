# 示例命令

## 1) 基础检索（默认返回20篇）
```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration clonality" \
  --start-date 2020/01/01 \
  --end-date 2026/12/31
```

## 2) 仅保留有摘要 + 限制返回10篇
```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration enhancer" \
  --start-date 2018/01/01 \
  --end-date 2026/12/31 \
  --retmax 10 \
  --has-abstract-only
```

## 3) 限定文章类型为 review 与 clinical trial
```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration cervical cancer" \
  --start-date 2015/01/01 \
  --end-date 2026/12/31 \
  --article-types review "clinical trial" \
  --output-prefix results/pubmed_search/hpv_review_trial
```

## 4) 关闭翻译（调试）
```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration" \
  --start-date 2024/01/01 \
  --end-date 2026/12/31 \
  --translate-engine none
```
