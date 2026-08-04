from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# =====================================================
# Define file paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent
    / "Dataset"
    / "cleaned"
    / "cleaned_customer_churn.csv"
)

IMAGES_PATH = BASE_DIR.parent / "Images"

IMAGES_PATH.mkdir(parents=True, exist_ok=True)

# =====================================================
# Load dataset
# =====================================================

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print(df.shape)

# =====================================================
# Churn Distribution
# =====================================================

churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(6, 5))

plt.bar(
    churn_counts.index,
    churn_counts.values,
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(IMAGES_PATH / "churn_distribution.png", dpi=300)

plt.show()

print("\nChurn Distribution")
print(churn_counts)

# =====================================================
# Gender Distribution
# =====================================================

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(6, 5))

plt.bar(
    gender_counts.index,
    gender_counts.values,
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(IMAGES_PATH / "gender_distribution.png", dpi=300)

plt.show()

print("\nGender Distribution")
print(gender_counts)

# =====================================================
# Contract Distribution
# =====================================================

contract_counts = df["Contract"].value_counts()

plt.figure(figsize=(7, 5))

plt.bar(
    contract_counts.index,
    contract_counts.values,
)

plt.title("Contract Type Distribution")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.xticks(rotation=10)

plt.tight_layout()

plt.savefig(IMAGES_PATH / "contract_distribution.png", dpi=300)

plt.show()

print("\nContract Distribution")
print(contract_counts)

# =====================================================
# Internet Service Distribution
# =====================================================

internet_counts = df["InternetService"].value_counts()

plt.figure(figsize=(7, 5))

plt.bar(
    internet_counts.index,
    internet_counts.values,
)

plt.title("Internet Service Distribution")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(IMAGES_PATH / "internet_service_distribution.png", dpi=300)

plt.show()

print("\nInternet Service Distribution")
print(internet_counts)

# =====================================================
# Payment Method Distribution
# =====================================================

payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(9, 5))

plt.bar(
    payment_counts.index,
    payment_counts.values,
)

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20, ha="right")

plt.tight_layout()

plt.savefig(IMAGES_PATH / "payment_method_distribution.png", dpi=300)

plt.show()

print("\nPayment Method Distribution")
print(payment_counts)

print("\nEDA COMPLETED SUCCESSFULLY")