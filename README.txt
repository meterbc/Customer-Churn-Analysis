# Customer Churn Analysis

An end-to-end customer churn analytics project using **Python, SQL Server, and Power BI**. This project explores customer behavior, identifies factors associated with customer churn, and transforms raw data into actionable business insights.

![Customer Churn Dashboard](Images/dashboard.png)

## Project Overview

Customer churn is a critical challenge for subscription-based businesses. Understanding why customers leave helps companies improve retention strategies, optimize revenue, and make data-driven decisions.

The objective of this project is to analyze the IBM Telco Customer Churn dataset through a complete data analytics workflow, starting with data cleaning and exploratory analysis and ending with SQL-based business analysis and an interactive Power BI dashboard.

## Business Objectives

- Analyze customer churn behavior and retention patterns.
- Identify customer segments with higher churn rates.
- Explore the relationship between customer characteristics and churn.
- Analyze revenue, contract types, payment methods, and service subscriptions.
- Develop business-oriented KPIs and interactive visualizations.
- Generate actionable insights to support customer retention strategies.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| SQL Server | Data storage and management |
| SQL | Business queries and KPI analysis |
| SQLAlchemy | Database connectivity |
| pyodbc | SQL Server connection |
| Power BI | Interactive dashboard development |
| Git & GitHub | Version control |

## Project Structure

```text
Customer-Churn-Analysis/
│
├── Dataset/
│   ├── raw/
│   └── cleaned/
│
├── Images/
│   ├── dashboard.png
│   ├── churn_distribution.png
│   ├── gender_distribution.png
│   ├── contract_distribution.png
│   ├── internet_service_distribution.png
│   └── payment_method_distribution.png
│
├── PowerBI/
│   └── Customer_Churn_Dashboard.pbix
│
├── Python/
│   ├── 01_data_cleaning.py
│   ├── 02_exploratory_data_analysis.py
│   ├── 03_business_analysis.py
│   ├── 04_database_connection.py
│   └── 05_load_to_sql.py
│
├── SQL/
│   ├── 01_create_database.sql
│   ├── 02_create_table.sql
│   └── 03_business_queries.sql
│
├── requirements.txt
└── README.md
```

## Project Workflow

```text
Raw Dataset
     |
     v
Data Cleaning (Python)
     |
     v
Exploratory Data Analysis
     |
     v
Business Analysis
     |
     v
SQL Server Database
     |
     v
SQL Queries & KPI Analysis
     |
     v
Power BI Dashboard
     |
     v
Business Insights
```

## Data Cleaning & Preprocessing

Data preparation was performed using Python and Pandas.

Key steps:

- Imported and inspected the raw dataset.
- Examined dataset dimensions, column types, and missing values.
- Converted `TotalCharges` into a numeric data type.
- Identified invalid and missing values.
- Removed records with missing `TotalCharges`.
- Exported the cleaned dataset for further analysis.

## Exploratory Data Analysis (EDA)

Exploratory analysis was conducted to understand customer characteristics and identify patterns in the dataset.

The analysis includes:

- Customer churn distribution
- Gender distribution
- Contract type distribution
- Internet service distribution
- Payment method distribution

Visualizations were generated using Matplotlib.

## SQL Server & Business Analysis

The cleaned dataset was transferred into Microsoft SQL Server.

The SQL analysis focuses on business-oriented questions, including:

- Total customer count
- Overall churn rate
- Churn rate by contract type
- Churn rate by payment method
- Churn rate by internet service
- Average monthly and total charges
- Average customer tenure
- Revenue by contract type
- Revenue by internet service
- Customer segmentation
- High-risk customer segments
- Executive KPI summary
- Customer lifetime groups

## Key Business Insights

The analysis highlights several important churn patterns:

- The overall customer churn rate is approximately **26.6%**.
- Customers with **Month-to-Month contracts** have the highest churn rate.
- Customers using **Electronic Check** as their payment method are more likely to churn.
- Customers with **Fiber Optic** internet service demonstrate higher churn.
- Churned customers have higher average monthly charges.
- Customers with longer tenure are more likely to remain with the company.

These findings can help businesses identify customers who may require targeted retention strategies.

## Power BI Dashboard

An interactive Power BI dashboard was developed to present the results in a business-friendly format.

The dashboard includes:

### Key Performance Indicators

- Total Customers
- Churn Rate
- Total Revenue
- Average Monthly Charge
- Average Customer Tenure

### Customer Analysis

- Churn by Contract
- Churn by Payment Method
- Churn by Internet Service
- Interactive Filters

The dashboard enables users to explore customer segments and evaluate churn patterns through interactive visualizations.

## Dataset

This project uses the **IBM Telco Customer Churn Dataset**, which contains customer demographic information, subscription details, billing information, and churn status.

The dataset includes features such as:

- CustomerID
- Gender
- SeniorCitizen
- Contract
- InternetService
- PaymentMethod
- MonthlyCharges
- TotalCharges
- Tenure
- Churn

**Dataset Source:** [IBM Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/meterbc/Customer-Churn-Analysis.git

cd Customer-Churn-Analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Dataset

Download the IBM Telco Customer Churn dataset and place the raw CSV file in:

```text
Dataset/raw/Telco-Customer-Churn.csv
```

### 4. Run Python Scripts

Execute the scripts in the following order:

```bash
python Python/01_data_cleaning.py

python Python/02_exploratory_data_analysis.py

python Python/03_business_analysis.py
```

### 5. Configure SQL Server

- Install Microsoft SQL Server and the required ODBC driver.
- Update the server and database connection settings in the Python scripts.
- Execute the SQL scripts in the following order:

```text
SQL/01_create_database.sql
SQL/02_create_table.sql
```

### 6. Load Data into SQL Server

Run the database connection test and data loading scripts after configuring your SQL Server connection:

```bash
python Python/04_database_connection.py

python Python/05_load_to_sql.py
```

### 7. Execute Business Queries

Run:

```text
SQL/03_business_queries.sql
```

### 8. Open the Power BI Dashboard

Open the `.pbix` file located in the `PowerBI` folder using Power BI Desktop.

Configure the data source connection if necessary.

## Author

**Mete Arabacı**

Industrial Engineering Student

[GitHub](https://github.com/meterbc)
