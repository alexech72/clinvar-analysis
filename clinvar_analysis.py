import pandas as pd
import biobricks

# Load ClinVar assets
clinvar = biobricks.assets("clinvar")

# Load variant summary table
variants = pd.read_parquet(clinvar.variant_summary_parquet)

print("Total variants:", len(variants))

# Count clinical significance categories
clin_sig_counts = (
    variants["ClinicalSignificance"]
    .value_counts(dropna=False)
    .head(15)
)

print("\nTop Clinical Significance Categories:")
print(clin_sig_counts)

# Save results for GitHub
clin_sig_counts.to_csv("clinical_significance_counts.csv")

print("\nSaved clinical_significance_counts.csv")

# Analyze conflicting interpretations
conflicts = variants[
    variants["ClinicalSignificance"]
    .str.contains("Conflicting", na=False)
]

print("\nConflicting interpretations count:", len(conflicts))

top_conflict_genes = (
    conflicts["GeneSymbol"]
    .value_counts()
    .head(10)
)

print("\nTop genes with conflicting interpretations:")
print(top_conflict_genes)

top_conflict_genes.to_csv("top_conflicting_genes.csv")


