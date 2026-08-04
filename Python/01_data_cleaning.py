from pathlib import Path
import pandas as pd

# =====================================================
# Define file paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = BASE_DIR.parent / "Dataset" / "raw" / "Telco-Customer-Churn.csv"
CLEANED_DATA_PATH = (
    BASE_DIR.parent
    / "Dataset"
    / "cleaned"
    / "cleaned_customer_churn.csv"
)

# =====================================================
# Load the dataset
# =====================================================

df = pd.read_csv(RAW_DATA_PATH)

# =====================================================
# Basic Dataset Overview
# =====================================================

print("=" * 70)
print("FIRST 5 ROWS")
print("=" * 70)
print(df.head())

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)
df.info()

print("\n" + "=" * 70)
print("DATASET SHAPE")
print("=" * 70)
print(df.shape)

print("\n" + "=" * 70)
print("COLUMN NAMES")
print("=" * 70)
print(df.columns.tolist())

print("\n" + "=" * 70)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 70)
print(df.isnull().sum())

print("\n" + "=" * 70)
print("NUMERICAL SUMMARY")
print("=" * 70)
print(df.describe())

print("\n" + "=" * 70)
print("CATEGORICAL SUMMARY")
print("=" * 70)
print(df.describe(include="str"))

# =====================================================
# Data Cleaning
# =====================================================

print("\n" + "=" * 70)
print("CONVERTING 'TotalCharges' TO NUMERIC")
print("=" * 70)

# Convert TotalCharges to numeric
# Invalid values (blank spaces) become NaN
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(f"Data Type : {df['TotalCharges'].dtype}")
print(f"Missing Values After Conversion : {df['TotalCharges'].isna().sum()}")

print("\nRows with Missing TotalCharges:")
print(
    df[df["TotalCharges"].isna()][
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges"]
    ]
)

# =====================================================
# Remove Missing Values
# =====================================================

print("\n" + "=" * 70)
print("REMOVING ROWS WITH MISSING TotalCharges")
print("=" * 70)

rows_before = len(df)

df = df.dropna(subset=["TotalCharges"])

rows_after = len(df)

print(f"Rows Before Cleaning : {rows_before}")
print(f"Rows After Cleaning  : {rows_after}")
print(f"Rows Removed         : {rows_before - rows_after}")

# =====================================================
# Final Missing Value Check
# =====================================================

print("\n" + "=" * 70)
print("FINAL MISSING VALUE CHECK")
print("=" * 70)
print(df.isnull().sum())

# =====================================================
# Save Cleaned Dataset
# =====================================================

CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(CLEANED_DATA_PATH, index=False)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)
print(f"Cleaned dataset saved to:\n{CLEANED_DATA_PATH}")

print("\nFinal Dataset Shape:")
print(df.shape)