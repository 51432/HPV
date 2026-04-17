# HPV 整合克隆性与局部调控重塑研究仓库

> 一个以生物学问题为驱动、以机制研究为核心、支持可复现分析的科研仓库。  
> 主线：**HPV 克隆性整合 → 局部顺式调控重塑 → 邻近宿主基因持续激活**。

## 项目定位

本仓库**不是**单纯的 HPV 整合检测工具开发项目，而是用于组织以下工作：
- 围绕核心科学问题构建可检验假说；
- 进行结构化文献调研与证据沉淀；
- 规划并执行多组学机制分析；
- 规范化管理数据、脚本、结果与图表，确保可复现。

当前研究动机：
1. HPV 整合事件在样本间存在克隆性差异；
2. HPV 整合位点附近基因常出现过表达。

核心科学问题：
- HPV 整合是否会改变局部基因组结构/染色质开放性/顺式调控环境，从而驱动邻近基因持续激活？
- 高克隆性整合事件是否更可能引发上述效应，并在肿瘤演化中被选择保留？

## 核心假说框架

### 主假说
- **H1（局部调控重塑）**：HPV 整合可重构局部顺式调控环境，导致邻近基因表达上调。
- **H2（克隆性-选择耦合）**：具有更强激活效应的整合事件更易呈现高克隆性并被保留。

### 优先机制路径（建议顺序）
1. 局部染色质开放性增强
2. 增强子劫持 / 增强子重连
3. CTCF/TAD/局部 3D 边界扰动
4. 局部拷贝数增益与复杂结构变异共驱动
5. 复杂扩增单元或 ecDNA 相关机制（若数据支持）

### 备选解释（需排除）
- 观察到的表达升高由广泛 CNV、肿瘤纯度或细胞状态变化驱动，而非整合局部效应；
- 高克隆性仅代表事件发生更早，不代表功能选择优势。

## 研究模块（Aims）

1. 整合事件整理与克隆性量化
2. 邻近基因异常表达与距离衰减分析
3. 调控环境注释（开放性/增强子/3D/CN/SV）
4. productive integration 筛选与候选驱动位点排序
5. 机制模型整合与替代假说检验

详见：
- `docs/project_scope.md`
- `docs/biological_hypothesis.md`
- `docs/literature_review_plan.md`
- `docs/analysis_plan.md`
- `docs/risk_and_alternatives.md`

## 仓库目录建议

```text
.
├── README.md
├── docs/
│   ├── project_scope.md
│   ├── biological_hypothesis.md
│   ├── literature_review_plan.md
│   ├── analysis_plan.md
│   └── risk_and_alternatives.md
├── refs/
│   └── literature/                 # 文献笔记与证据表
├── metadata/                       # 样本清单、注释版本、字段字典
├── workflow/                       # 工作流定义与运行清单
├── scripts/                        # 分析脚本（R/Python/bash）
├── notebooks/                      # 探索性分析 notebook
├── data/
│   ├── raw/                        # 原始数据（建议只放索引/清单）
│   └── processed/                  # 衍生数据矩阵与中间结果
├── results/                        # 表格结果与阶段输出
├── figures/                        # 图表与面板源文件
└── issues/
    └── issues_draft.md             # 可直接复制创建的 issue 草稿
```

## 里程碑（草案）

- **M1：课题定义 + 文献基线**
- **M2：整合/克隆性数据模型 + 质量控制**
- **M3：局部 cis 效应量化 + 候选 productive integration**
- **M4：多组学机制验证与稳健性分析**
- **M5：结果冻结与复现检查（论文级输出）**

## 工作原则

- 生物学问题优先，工具开发服务于问题验证；
- 每一步分析都要映射到可证伪的科学问题；
- 明确数据版本、注释版本与参数来源；
- 区分探索性结果与冻结版本结果。

## 当前阶段

当前仓库已完成前期规划骨架，适合进入：
1) 文献证据矩阵构建；2) 事件级数据整理；3) Aim1/Aim2 原型分析。

---

## PubMed 文献检索 Skill（中文说明）

本仓库已提供可复用 skill：`skills/pubmed-search/`，用于在固定高影响期刊范围内调用 PubMed E-utilities 检索文献，并导出中英文结果到 `results/pubmed_search/`。

### 功能
- 支持参数：关键词、起止日期、返回上限、仅有摘要筛选、文章类型筛选；
- 获取字段：PMID、英文标题、发表日期、期刊名、PubMed 链接、英文摘要；
- 自动生成中文标题与中文摘要（可关闭翻译）；
- 导出 Markdown 表格与 CSV。

### 快速开始

```bash
python skills/pubmed-search/scripts/pubmed_search.py \
  --keywords "HPV integration clonality" \
  --start-date 2020/01/01 \
  --end-date 2026/12/31 \
  --retmax 20
```

### 相关文档
- Skill 说明：`skills/pubmed-search/SKILL.md`
- 示例命令：`skills/pubmed-search/references/example_commands.md`
- 测试输入输出示例：`skills/pubmed-search/references/test_io_examples.md`

