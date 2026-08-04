from pathlib import Path
import pandas as pd
import pyodbc

# =====================================================
# File Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent
    / "Dataset"
    / "cleaned"
    / "cleaned_customer_churn.csv"
)

# =====================================================
# Read Dataset
# =====================================================

df = pd.read_csv(DATA_PATH)

# =====================================================
# SQL Server Connection
# =====================================================

connection = pyodbc.connect(
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=Mete\SQLEXPRESS;"
    r"DATABASE=CustomerChurnDB;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"
)

cursor = connection.cursor()

# =====================================================
# Clear Existing Data
# =====================================================

cursor.execute("DELETE FROM CustomerChurn")

# =====================================================
# SQL Insert Statement
# =====================================================

insert_query = """
INSERT INTO CustomerChurn
(
CustomerID,
Gender,
SeniorCitizen,
Partner,
Dependents,
Tenure,
PhoneService,
MultipleLines,
InternetService,
OnlineSecurity,
OnlineBackup,
DeviceProtection,
TechSupport,
StreamingTV,
StreamingMovies,
Contract,
PaperlessBilling,
PaymentMethod,
MonthlyCharges,
TotalCharges,
Churn
)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""

# =====================================================
# Convert DataFrame to Tuple List
# =====================================================

rows = list(df.itertuples(index=False, name=None))

# =====================================================
# Bulk Insert
# =====================================================

cursor.fast_executemany = True
cursor.executemany(insert_query, rows)

connection.commit()

print("=" * 60)
print("DATA LOADED SUCCESSFULLY")
print("=" * 60)
print(f"Rows Inserted: {len(rows)}")

cursor.close()
connection.close()