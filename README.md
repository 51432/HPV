# HPV Integration Clonality and Local Regulatory Rewiring

> A biology-driven, mechanism-focused, and reproducible research repository for studying the axis:
> **HPV integration clonality → local cis-regulatory remodeling → sustained activation of nearby host genes**.

## Project Positioning

This repository is **not** primarily an HPV integration-caller development project.  
It is designed for:
- Mechanism-oriented hypothesis development;
- Structured literature synthesis;
- Stepwise multi-omics analysis planning and execution;
- Reproducible organization of data, code, results, and figures.

Core research motivation:
1. HPV integration events show heterogeneous clonality across samples.
2. Genes near integration breakpoints are frequently overexpressed.

Main scientific question:
- Does HPV integration remodel local genome/chromatin/regulatory architecture (e.g., accessibility, enhancer wiring, 3D boundaries, CN/SV context), thereby driving persistent activation of nearby host genes?
- Are high-clonality integration events more likely to induce such activation and be retained under tumor evolution/selection?

## Core Hypothesis Framework

### Primary hypotheses
- **H1 (cis-regulatory rewiring):** HPV integration can reconfigure local cis-regulatory context and elevate nearby host-gene expression.
- **H2 (clonality-selection coupling):** Integration events with stronger gene-activating/regulatory effects show higher clonality and are more likely to be selected.

### Mechanistic sub-hypotheses (priority order)
1. Local chromatin accessibility gain (ATAC-like signal increase around breakpoints)
2. Enhancer hijacking / enhancer adoption near integration sites
3. CTCF/TAD or local 3D boundary perturbation
4. Local CN gain/amplification and/or complex SV-mediated activation
5. Episomal/integrated hybrid states or ecDNA-related amplification effects (if data supports)

### Alternative hypotheses
- Apparent cis-effects are confounded by broad CNA programs, lineage-state transitions, purity, or stromal composition.
- High clonality reflects early timing or mutational process exposure, not selective advantage from expression activation.

## Planned Research Modules (Aims)

1. **Integration event curation and clonality quantification**
2. **Nearby gene dysregulation and distance-decay cis-effect analysis**
3. **Regulatory context annotation (accessibility/enhancer/3D/SV/CN)**
4. **Productive integration identification and candidate driver loci ranking**
5. **Mechanistic model integration and falsification analysis**

See details in:
- `docs/project_scope.md`
- `docs/biological_hypothesis.md`
- `docs/literature_review_plan.md`
- `docs/analysis_plan.md`
- `docs/risk_and_alternatives.md`

## Suggested Repository Structure

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
│   └── literature/                 # paper notes, PDFs index, extracted evidence tables
├── metadata/                       # sample sheets, cohort manifests, annotation versions
├── workflow/                       # workflow specs (e.g., Snakemake/Nextflow plans), run manifests
├── scripts/                        # modular analysis scripts (R/Python/bash)
├── notebooks/                      # exploratory notebooks (clearly versioned/frozen)
├── data/
│   ├── raw/                        # immutable inputs (tracked via pointers/manifest)
│   └── processed/                  # derived matrices/tables
├── results/                        # final tables and intermediate analysis outputs
├── figures/                        # publication-quality figures and panel sources
└── issues/
    └── issues_draft.md             # copy-ready GitHub issue drafts
```

## Milestone Roadmap (Draft)

- **M1: Question framing + literature baseline**
- **M2: Event/clonality data model + QC baseline**
- **M3: Cis-effect quantification + candidate productive integrations**
- **M4: Multi-omics mechanism validation and robustness tests**
- **M5: Manuscript-grade outputs and reproducibility freeze**

## Working Principles

- Biology-first, tool-second.
- Every analysis step should map to a falsifiable biological question.
- Keep provenance explicit (data version, annotation version, software versions).
- Separate exploratory vs. frozen analysis outputs.

## Current Stage

This commit establishes the **planning and documentation scaffold** for early-phase project setup.
