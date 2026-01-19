# ClinVar Variant Analysis

## Overview
This project performs an exploratory **biomedical informatics analysis** of ClinVar genetic variant data using Python and BioBricks. The goal is to examine how genetic variants are classified clinically and to identify genes with a high number of conflicting clinical interpretations.

ClinVar is a public database that aggregates information about genomic variation and its relationship to human health.

## Why This Matters (Informatics Context)
Conflicting variant interpretations in ClinVar can affect clinical decision-making, genetic counseling, and downstream research. Quantifying where and how these conflicts occur helps identify genes and regions where evidence is limited, evolving, or inconsistent.

## Dataset
- Source: ClinVar (accessed via BioBricks)
- Total variants analyzed: ~4.6 million
- Data format: Parquet

## Methods
- Loaded ClinVar variant tables using BioBricks
- Performed data exploration using pandas
- Aggregated variants by clinical significance
- Identified variants with conflicting interpretations
- Ranked genes by number of conflicting interpretations

## Key Findings
- The most common classification was **Uncertain significance**
- Over **200,000 variants** had conflicting clinical interpretations
- Genes such as **BRCA2, BRCA1, and TTN** showed the highest number of conflicts
- These results highlight ongoing challenges in clinical variant interpretation

## Files
- `clinvar_analysis.py` — Python script used for loading and analyzing ClinVar data
- `clinical_significance_counts.csv` — Aggregated counts by clinical significance
- `top_conflicting_genes.csv` — Genes ranked by number of conflicting interpretations

## Reproducibility and Data Management
ClinVar data is accessed via BioBricks as versioned Parquet assets rather than manual downloads. This approach supports reproducible analysis, consistent data access across environments, and mirrors real-world biomedical informatics workflows.

## Technologies Used
- Python
- pandas
- BioBricks
- Parquet datasets

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas biobricks


