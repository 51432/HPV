# 文献调研规划（Literature Review Plan）

## 1. 调研目标
建立一套可检索、可比较、可更新的证据框架，围绕主线：
**HPV整合克隆性 ↔ 局部调控重塑 ↔ 邻近基因持续激活**。

## 2. 文献类别与关键问题

## A. HPV整合分子机制基础研究
**要回答：**
- HPV整合发生机制与断点特征是什么？
- 宿主DNA修复通路（NHEJ/MMEJ等）如何参与？
- 病毒-宿主连接结构常见模式有哪些？

## B. 整合与邻近基因表达关系研究
**要回答：**
- 邻近基因上调的证据强度如何？
- 效应距离范围、方向性、癌种差异如何？
- 是否有重复验证的高频候选基因/位点？

## C. 调控重塑机制研究（ATAC/增强子/3D）
**要回答：**
- 是否观察到整合附近开放性增强？
- 是否存在增强子劫持或异常环路证据？
- CTCF/TAD边界是否受整合或重排影响？

## D. 结构变异与拷贝数背景研究
**要回答：**
- 局部扩增/复杂SV是否与整合共现并解释表达升高？
- 如何区分“整合驱动”与“扩增驱动”？

## E. 克隆性、演化与选择压力研究
**要回答：**
- 克隆性如何定义与估计？
- 高克隆性位点是否与功能表型关联？
- 有无纵向样本/单细胞证据支持选择保留？

## F. 方法学参考（辅助）
**要回答：**
- 可用哪些integration calling / annotation / interpretation流程？
- 方法误差来源、比较基准与适用场景是什么？

---

## 3. 调研优先级（建议顺序）

1. **高优先级（Week 1–2）**：A + B + E
   - 先确立“整合—表达—克隆性”主线是否有坚实证据。
2. **中高优先级（Week 2–4）**：C + D
   - 进一步寻找“机制层”可检验桥梁。
3. **中优先级（持续）**：F
   - 作为技术支撑，不喧宾夺主。

---

## 4. 结构化记录模板（建议CSV/TSV + Markdown）

## 表1：`refs/literature/paper_catalog.csv`
字段建议：
- paper_id
- title
- year
- journal
- cancer_type
- sample_type
- data_modalities (WGS/RNA/ATAC/Hi-C/CNV/SV/...)
- integration_detection_method
- clonality_definition
- key_findings
- evidence_level (descriptive/associative/mechanistic/functional)
- limitations
- reproducibility_assets (code/data availability)
- priority (high/medium/low)

## 表2：`refs/literature/evidence_matrix.csv`
按“假说—证据”组织：
- hypothesis_id (H1/H2/AH1...)
- mechanism_class (accessibility/enhancer/3D/CN/SV/evolution)
- paper_id
- claim
- evidence_type
- cohort_size
- effect_direction
- robustness_notes
- confidence_score (1-5)

## 表3：`refs/literature/method_benchmark_notes.csv`
- method_name
- input_data
- output_definition
- strengths
- known_bias
- required_qc
- suitable_use_case_in_this_project

## 表4：`refs/literature/candidate_loci_registry.csv`
- locus_id
- virus_type
- chromosome
- breakpoint_region
- nearby_gene
- reported_expression_effect
- reported_clonality_pattern
- mechanism_annotation
- validation_status

---

## 5. GitHub文档化建议

- `docs/literature_review_plan.md`：调研策略、优先级、模板说明（本文件）
- `refs/literature/reading_log.md`：按周记录阅读进展与结论摘要
- `refs/literature/key_papers.md`：高优先级论文一页式总结
- `refs/literature/evidence_matrix.csv`：量化证据矩阵
- `refs/literature/open_questions.md`：未解决问题与后续验证建议

---

## 6. 质量控制与更新频率

- 每周最少一次更新 `reading_log.md` 与 `paper_catalog.csv`；
- 每两周复核一次证据分级（避免单篇文献过度影响）；
- 对高影响结论要求至少2类独立证据来源（例如跨队列或跨组学）。
