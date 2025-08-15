# ===============================================================
# Lloyds Bank Customer Data - Full EDA Script
# Author: [Your Name]
# Date: [Date]
# ===============================================================

# ------------------------------
# 1. Import Required Libraries
# ------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid", palette="muted")

# ------------------------------
# 2. Load Dataset
# ------------------------------
# Load without headers to inspect structure
lloydsfinal = pd.read_csv("final_dataset.csv", header=None)
print("\nInitial load without headers:\n", lloydsfinal.head())

# Assign proper column names
lloydsfinal.columns = [
    "customer_id",
    "customer_code",
    "age",
    "gender",
    "region",
    "account_type",
    "account_tenure_years",
    "balance_gbp",
    "transactions_count",
    "total_transaction_amount_gbp",
    "avg_transaction_amount_gbp",
    "loan_amount_gbp",
    "interest_rate",
    "loan_status",
    "complaints_count",
    "churn_label"
]
print("\nAssigned column names:\n", lloydsfinal.columns.tolist())

# Reload CSV with headers applied
lloydsfinal = pd.read_csv("final_dataset.csv")
print("\nPreview of dataset:\n", lloydsfinal.head())

# ------------------------------
# 3. Data Overview
# ------------------------------
print("\n--- Dataset Info ---")
print(lloydsfinal.info())

print("\n--- Summary Statistics (Numeric) ---")
print(lloydsfinal.describe())

print("\n--- Missing Values ---")
print(lloydsfinal.isnull().sum())

print("\nFirst 5 rows:\n", lloydsfinal.head())
print("\nLast 5 rows:\n", lloydsfinal.tail())

# ------------------------------
# 4. Univariate Analysis - Numeric
# ------------------------------
# Histograms for numeric columns
lloydsfinal.hist(bins=30, figsize=(15, 10))
plt.suptitle("Numeric Column Distributions", fontsize=16)
plt.show()

# ------------------------------
# 5. Correlation Analysis
# ------------------------------
# Full correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(lloydsfinal.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (All Numeric Columns)", fontsize=14)
plt.show()

# Numeric-only correlation heatmap (extra from Script 2)
numeric_cols = lloydsfinal.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(12, 8))
sns.heatmap(lloydsfinal[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Numeric Columns Only)", fontsize=16)
plt.show()

# ------------------------------
# 6. Categorical Data Overview
# ------------------------------
categorical_cols = lloydsfinal.select_dtypes(include=['object']).columns.tolist()
print("\nCategorical columns:", categorical_cols)

# Region distribution
plt.figure(figsize=(10, 5))
sns.countplot(x="region", data=lloydsfinal, order=lloydsfinal["region"].value_counts().index)
plt.xticks(rotation=45)
plt.title("Customer Count by Region")
plt.show()

# Loan status by gender
plt.figure(figsize=(8, 5))
sns.countplot(x="gender", hue="loan_status", data=lloydsfinal)
plt.title("Loan Status by Gender")
plt.show()

# ------------------------------
# 7. Key Numeric Distributions
# ------------------------------
# Balance distribution
plt.figure(figsize=(8, 5))
sns.histplot(lloydsfinal["balance_gbp"], bins=30, kde=True)
plt.title("Distribution of Account Balances")
plt.xlabel("Balance (GBP)")
plt.ylabel("Number of Customers")
plt.show()

# Loan amount distribution
plt.figure(figsize=(8,5))
sns.histplot(lloydsfinal['loan_amount_gbp'], bins=30, kde=True)
plt.title("Loan Amount Distribution")
plt.show()

# Loan Amount vs Interest Rate
plt.figure(figsize=(8, 5))
sns.scatterplot(x="loan_amount_gbp", y="interest_rate", hue="loan_status", data=lloydsfinal)
plt.title("Loan Amount vs Interest Rate")
plt.xlabel("Loan Amount (GBP)")
plt.ylabel("Interest Rate (%)")
plt.show()

# ------------------------------
# 8. Summary Stats - Mean & Median
# ------------------------------
mean_values = lloydsfinal.mean(numeric_only=True)
print("\nMean values:\n", mean_values)

median_values = lloydsfinal.median(numeric_only=True)
print("\nMedian values:\n", median_values)

# ------------------------------
# 9. Detailed Distributions & Outlier Checks
# ------------------------------
# Histograms with KDE for each numeric column
plt.figure(figsize=(15, 12))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot((len(numeric_cols) // 3) + 1, 3, i)
    sns.histplot(lloydsfinal[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# Boxplots for outlier detection
plt.figure(figsize=(15, 12))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot((len(numeric_cols) // 3) + 1, 3, i)
    sns.boxplot(y=lloydsfinal[col])
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# ------------------------------
# 10. Cross-Tabulations
# ------------------------------
print("\nRegion vs Loan Status Crosstab:\n", pd.crosstab(lloydsfinal['region'], lloydsfinal['loan_status']))

# ------------------------------
# 11. Categorical Summary
# ------------------------------
for col in categorical_cols:
    print(f"\nColumn: {col}")
    print(lloydsfinal[col].value_counts())
    print("-" * 40)

# ------------------------------
# 12. Final Key Plots
# ------------------------------
# Gender count
plt.figure(figsize=(6,4))
sns.countplot(x="gender", data=lloydsfinal)
plt.title("Customer Count by Gender")
plt.show()

# Loan status count
plt.figure(figsize=(6,4))
sns.countplot(x="loan_status", data=lloydsfinal)
plt.title("Customer Count by Loan Status")
plt.show()

# Churn label count
plt.figure(figsize=(6,4))
sns.countplot(x="churn_label", data=lloydsfinal)
plt.title("Customer Count by Churn Label")
plt.show()

# Final correlation matrix
plt.figure(figsize=(10,8))
sns.heatmap(lloydsfinal.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Final Correlation Matrix")
plt.show()
