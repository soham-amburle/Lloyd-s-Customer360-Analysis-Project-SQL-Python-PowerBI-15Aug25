## Explore "Lloyds Customer 360 Analysis" Project Resources

[![SQL](https://img.shields.io/badge/SQL-Database-blue)](sql/data_cleanup_and_merge.sql)  
[![Python](https://img.shields.io/badge/Python-Exploratory%20Data%20Analysis-yellow)](python/eda_analysis.ipynb)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-green)](dashboards/)

15 August, 2025

# Lloyds Finance Project : Customer 360° Analysis

## Project Overview
This project aims to build a comprehensive **Customer 360° view** for Lloyds Bank customers by consolidating multiple datasets (complaints, customers, loans, and transactions), performing exploratory data analysis (EDA), and developing insightful dashboards. The main objective is to understand customer demographics, transaction behavior, loan patterns, and retention opportunities.

---

## Project Workflow

### 1. Business Problem
- Understanding the key business objectives: improving customer insights, optimizing loan strategies, and enhancing customer retention.
- Key questions:
  - Who are our most valuable customers?
  - What are transaction and loan behavior patterns?
  - Which factors influence churn and retention?

---

### 2. Data Collection & SQL Data Processing
Multiple datasets were collected and loaded into SQL for exploration and cleaning:

**Datasets:**
- Customers (`customers.csv`)
- Transactions (`transactions.csv`)
- Loans (`loans.csv`)
- Complaints (`complaints.csv`)

**Steps Performed in SQL:**
1. Loaded the CSV files into the database tables.
2. Explored customer demographics:
   - Total customers, age, gender distribution, region-wise counts, account tenure, and average balances.
3. Explored transaction data:
   - Transaction counts, transaction amounts, category-wise analysis, top customers by transactions.
4. Explored loans data:
   - Total loans, loan status breakdown, average loan amount, interest rate analysis.
5. Explored complaints data:
   - Total complaints, complaint types, resolution times, complaints per customer.
6. Merged all datasets to create the `final_dataset`:
   - Aggregated transactions and complaints per customer.
   - Combined with customer demographics and loan information.
   - Resulting table forms the **Customer 360° view - final_dataset.csv**, ready for Python EDA.

---

### 3. Python Exploratory Data Analysis (EDA)
Using the `final_dataset.csv` generated in SQL, detailed analysis was conducted in Python:

**Key Steps:**
1. Loaded the dataset and assigned appropriate column names.
2. Data overview:
   - Dataset info, summary statistics, and missing values check.
3. Univariate analysis for numeric columns:
   - Histograms, KDE plots, and boxplots for outlier detection.
4. Correlation analysis:
   - Full correlation heatmaps and numeric-only correlation analysis.
5. Categorical analysis:
   - Countplots for region, gender, loan status, and churn labels.
   - Crosstabs for relationships like Region vs Loan Status.
6. Key numeric distributions:
   - Balance, loan amount, interest rates, transaction amounts.
7. Summary statistics:
   - Mean, median, and other key numeric indicators.
8. Final visualizations:
   - Plots for customer demographics, loan behavior, transactions, churn, and correlations.

---

### 4. Dashboards
Based on EDA insights, the following dashboards are planned for business reporting:

1. **Executive Overview**  
   - High-level summary of customer base, loan portfolio, transaction volume, and complaints.

2. **Customer Profile Dashboard**  
   - Demographics, account types, tenure, balances, and churn analysis.

3. **Loan & Balance Analysis**  
   - Loan distribution, average balances, interest rate comparisons, and loan status metrics.

4. **Transaction Behavior Dashboard**  
   - Transaction volumes by category, average amounts, and customer activity trends.

5. **Retention Recommendations & Action Plan**  
   - Insights on churn risk, complaint resolution impact, and targeted strategies for retention.

---

### 5. Final Report
- The final report consolidates SQL findings, Python EDA insights, and dashboard outputs.
- Highlights actionable insights and recommendations for improving customer engagement, retention, and financial planning.

---

## Technologies Used

- **SQL**: Data loading, cleaning, merging, aggregation. (PgAdmin)
- **Python (Pandas, Matplotlib, Seaborn)**: Exploratory Data Analysis, visualization (PyCharm)
- **Jupyter Notebook**: Interactive data exploration and analysis
- **Dashboard Tools**: Power BI

---

## Outcome

- Consolidated **Customer 360° view** dataset
- Comprehensive insights into customer demographics, transactions, loans, and complaints
- Data-driven recommendations for customer retention and engagement strategies
- 5 Visual dashboards for easy executive interpretation, and decision making

## Project Structure
```text
Lloyds_Finance_Project/
│
├── data/
│   ├── customers.csv
│   ├── transactions.csv
│   ├── loans.csv
│   └── complaints.csv
│
├── sql/
│   └── lloyds_customer_360.sql
│
├── python/
│   └── Lloyds_eda.ipynb
│
├── dashboards/
│   ├── dashboard 1 - executive_overview_dashboard.pdf and powerbi file
│   ├── dashboard 2 - customer_profile_dashboard.pdf and powerbi file
│   ├── dashboard 3 - loan_balance_analysis_dashboard.pdf and powerbi file
│   ├── dashboard 4 - transaction_behavior_dashboard.pdf and powerbi file
│   └── dashboard 5 - retention_recommendations_dashboard.pdf and powerbi file
│
└── README.md
