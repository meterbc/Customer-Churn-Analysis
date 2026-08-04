from pathlib import Path

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

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("BUSINESS ANALYSIS")
print("=" * 70)

# =====================================================
# Overall Churn Rate
# =====================================================

overall_churn_rate = (df["Churn"] == "Yes").mean() * 100

print(f"\nOverall Churn Rate: {overall_churn_rate:.2f}%")

# =====================================================
# Churn Rate by Contract
# =====================================================

contract_churn = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Contract")
print(contract_churn)

# =====================================================
# Churn Rate by Internet Service
# =====================================================

internet_churn = (
    df.groupby("InternetService")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Internet Service")
print(internet_churn)

# =====================================================
# Churn Rate by Payment Method
# =====================================================

payment_churn = (
    df.groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Payment Method")
print(payment_churn)

# =====================================================
# Churn Rate by Gender
# =====================================================

gender_churn = (
    df.groupby("gender")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print("\nChurn Rate by Gender")
print(gender_churn)

# =====================================================
# Churn Rate by Senior Citizen
# =====================================================

senior_churn = (
    df.groupby("SeniorCitizen")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print("\nChurn Rate by Senior Citizen")
print(senior_churn)

# =====================================================
# Churn Rate by Partner
# =====================================================

partner_churn = (
    df.groupby("Partner")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print("\nChurn Rate by Partner")
print(partner_churn)

# =====================================================
# Churn Rate by Dependents
# =====================================================

dependent_churn = (
    df.groupby("Dependents")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print("\nChurn Rate by Dependents")
print(dependent_churn)

# =====================================================
# Average Monthly Charges
# =====================================================

monthly_charge = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage Monthly Charges")
print(monthly_charge)

# =====================================================
# Average Total Charges
# =====================================================

total_charge = df.groupby("Churn")["TotalCharges"].mean()

print("\nAverage Total Charges")
print(total_charge)

# =====================================================
# Average Customer Tenure
# =====================================================

tenure = df.groupby("Churn")["tenure"].mean()

print("\nAverage Customer Tenure")
print(tenure)

# =====================================================
# Key Business Insights
# =====================================================

print("\n" + "=" * 70)
print("KEY BUSINESS INSIGHTS")
print("=" * 70)

highest_contract = contract_churn.idxmax()
highest_contract_rate = contract_churn.max()

highest_payment = payment_churn.idxmax()
highest_payment_rate = payment_churn.max()

highest_internet = internet_churn.idxmax()
highest_internet_rate = internet_churn.max()

print(
    f"• Customers with '{highest_contract}' contracts have the highest churn rate "
    f"({highest_contract_rate:.2f}%)."
)

print(
    f"• Customers using '{highest_payment}' have the highest churn rate "
    f"({highest_payment_rate:.2f}%)."
)

print(
    f"• Customers using '{highest_internet}' internet service have the highest churn rate "
    f"({highest_internet_rate:.2f}%)."
)

print(
    f"• Customers who churn pay an average monthly charge of "
    f"${monthly_charge['Yes']:.2f}."
)

print(
    f"• Customers who stay pay an average monthly charge of "
    f"${monthly_charge['No']:.2f}."
)

print(
    f"• Churned customers stay for an average of "
    f"{tenure['Yes']:.1f} months."
)

print(
    f"• Retained customers stay for an average of "
    f"{tenure['No']:.1f} months."
)

print("\nBusiness analysis completed successfully.")