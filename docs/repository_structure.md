# 建议的仓库目录树

```text
HPV/
├── README.md
├── docs/
│   ├── project_scope.md
│   ├── biological_hypothesis.md
│   ├── literature_review_plan.md
│   ├── analysis_plan.md
│   ├── risk_and_alternatives.md
│   ├── repository_structure.md
│   └── todo.md
├── refs/
│   └── literature/
│       ├── .gitkeep
│       ├── paper_catalog.csv                # 建议后续创建
│       ├── evidence_matrix.csv              # 建议后续创建
│       ├── method_benchmark_notes.csv       # 建议后续创建
│       └── candidate_loci_registry.csv      # 建议后续创建
├── metadata/
│   └── .gitkeep
├── workflow/
│   └── .gitkeep
├── scripts/
│   └── .gitkeep
├── notebooks/
│   └── .gitkeep
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
├── results/
│   └── .gitkeep
├── figures/
│   └── .gitkeep
└── issues/
    └── issues_draft.md
```

> 说明：`refs/literature/*.csv` 在当前阶段建议先定义模板字段，后续按文献调研进度逐步填充。
