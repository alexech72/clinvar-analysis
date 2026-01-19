# ClinVar Variant Analysis

This project performs exploratory analysis on the ClinVar database using Python and BioBricks.

## Overview
ClinVar is a public archive of reports on the relationships between human genetic variants and phenotypes.  
This analysis loads over 4.6 million variants and examines clinical significance trends and conflicts.

## Analysis Performed
- Loaded the full ClinVar variant dataset using BioBricks
- Counted variants by clinical significance category
- Identified variants with conflicting interpretations
- Ranked genes by number of conflicting submissions
- Exported summary statistics to CSV

## Key Findings
- Most variants are labeled **Uncertain Significance**
- Over **200,000 variants** have conflicting interpretations
- Genes with the highest conflicts include:
  - BRCA2
  - TTN
  - BRCA1
  - TSC2
  - MSH2

## Tools & Technologies
- Python
- Pandas
- BioBricks
- ClinVar

## Files
- `clinvar_analysis.py` — main analysis script
- `clinical_significance_counts.csv` — output data

## Why This Matters
Conflicting interpretations of genetic variants are a major challenge in clinical genomics and precision medicine.  
This analysis highlights genes and variants where disagreement is most common.
