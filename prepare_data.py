import pandas as pd

INPUT_FILE = "boxoffice_data_2024.csv"
OUTPUT_FILE = "boxoffice_clean.csv"

print("Reading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Original rows: {len(df)}")
print(f"Original columns: {len(df.columns)}")

# --------------------------------------------------
# Clean Year
# --------------------------------------------------

df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
).astype("Int64")

# --------------------------------------------------
# Clean Title
# --------------------------------------------------

df["Title"] = df["Title"].fillna("").astype(str).str.strip()

# --------------------------------------------------
# Clean Gross
# Example:
# "$234,760,478" -> 234760478
# --------------------------------------------------

df["Gross"] = (
    df["Gross"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Gross"] = pd.to_numeric(
    df["Gross"],
    errors="coerce"
).fillna(0).astype("int64")

# --------------------------------------------------
# Remove rows where Year or Title is missing
# --------------------------------------------------

df = df.dropna(subset=["Year"])
df = df[df["Title"] != ""]

# --------------------------------------------------
# Convert Year to normal integer
# --------------------------------------------------

df["Year"] = df["Year"].astype("int64")

# --------------------------------------------------
# Save cleaned dataset
# --------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaning completed.")
print(f"Final rows: {len(df)}")
print(f"Final columns: {len(df.columns)}")

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head().to_string(index=False))

print(f"\nSaved as: {OUTPUT_FILE}")