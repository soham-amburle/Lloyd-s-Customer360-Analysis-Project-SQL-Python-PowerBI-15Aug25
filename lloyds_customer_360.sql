/*********************************************************************
* Project: Lloyd's Finance Project
* Description: SQL scripts to load, explore, and merge customer,
*              transaction, loan, and complaint data to create a
*              Customer 360° view for analysis.
* Outcome: Generating a Final Data Set on which Python EDA would be done.
*********************************************************************/

/**************************************
* STEP 1: Load CSV Data into Tables
**************************************/

-- Load Customers
COPY customers
FROM 'C:\\lloyds_project\\data\\customers.csv'
DELIMITER ','
CSV HEADER;

-- Load Transactions
COPY transactions
FROM 'C:\\lloyds_project\\data\\transactions.csv'
DELIMITER ','
CSV HEADER;

-- Load Loans
COPY loans
FROM 'C:\\lloyds_project\\data\\loans.csv'
DELIMITER ','
CSV HEADER;

-- Load Complaints
COPY complaints
FROM 'C:\\lloyds_project\\data\\complaints.csv'
DELIMITER ','
CSV HEADER;


/**************************************
* STEP 2: Explore Customer Demographics
**************************************/

-- 1. Total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 2. Customers by region
SELECT region, COUNT(*) AS customer_count
FROM customers
GROUP BY region
ORDER BY customer_count DESC;

-- 3. Average balance by account type
SELECT account_type, ROUND(AVG(balance_gbp), 2) AS avg_balance
FROM customers
GROUP BY account_type;

-- 4. Gender distribution
SELECT gender, COUNT(*) AS count
FROM customers
GROUP BY gender;

-- 5. Average account tenure (years)
SELECT ROUND(AVG(account_tenure_years), 2) AS avg_tenure_years
FROM customers;


/**************************************
* STEP 3: Explore Transactions Data
**************************************/

-- 1. Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- 2. Transactions by category
SELECT category, COUNT(*) AS transaction_count
FROM transactions
GROUP BY category
ORDER BY transaction_count DESC;

-- 3. Total transaction amount by category
SELECT category, ROUND(SUM(amount_gbp), 2) AS total_amount
FROM transactions
GROUP BY category
ORDER BY total_amount DESC;

-- 4. Average transaction amount
SELECT ROUND(AVG(amount_gbp), 2) AS avg_transaction_amount
FROM transactions;

-- 5. Transactions per customer (top 10)
SELECT customer_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY customer_id
ORDER BY transaction_count DESC
LIMIT 10;


/**************************************
* STEP 4: Explore Loans Data
**************************************/

-- 1. Total number of loans
SELECT COUNT(*) AS total_loans
FROM loans;

-- 2. Loans by status
SELECT loan_status, COUNT(*) AS loan_count
FROM loans
GROUP BY loan_status
ORDER BY loan_count DESC;

-- 3. Average loan amount by status
SELECT loan_status, ROUND(AVG(loan_amount_gbp), 2) AS avg_loan_amount
FROM loans
GROUP BY loan_status;

-- 4. Average interest rate by status
SELECT loan_status, ROUND(AVG(interest_rate_percent), 2) AS avg_interest_rate
FROM loans
GROUP BY loan_status;


/**************************************
* STEP 5: Explore Complaints Data
**************************************/

-- 1. Total number of complaints
SELECT COUNT(*) AS total_complaints
FROM complaints;

-- 2. Complaints by type
SELECT complaint_type, COUNT(*) AS complaint_count
FROM complaints
GROUP BY complaint_type
ORDER BY complaint_count DESC;

-- 3. Average resolution time (days)
SELECT ROUND(AVG(resolution_days), 2) AS avg_resolution_days
FROM complaints;

-- 4. Complaints per customer (top 10)
SELECT customer_id, COUNT(*) AS complaint_count
FROM complaints
GROUP BY customer_id
ORDER BY complaint_count DESC
LIMIT 10;


/**************************************
* STEP 6: Merge Datasets into Final Dataset
* Goal: Create a "Customer 360° View"
**************************************/

-- Aggregate transactions per customer
CREATE TEMP TABLE transactions_summary AS
SELECT
    customer_id,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_gbp), 2) AS total_transaction_amount,
    ROUND(AVG(amount_gbp), 2) AS avg_transaction_amount
FROM transactions
GROUP BY customer_id;

-- Aggregate complaints per customer
CREATE TEMP TABLE complaints_summary AS
SELECT
    customer_id,
    COUNT(*) AS total_complaints,
    ROUND(AVG(resolution_days), 2) AS avg_resolution_days
FROM complaints
GROUP BY customer_id;

-- Combine customers + transaction summary + complaints summary + loan info
CREATE TABLE final_dataset AS
SELECT
    c.customer_id,
    c.name,
    c.age,
    c.gender,
    c.region,
    c.account_type,
    c.account_tenure_years,
    c.balance_gbp,
    t.total_transactions,
    t.total_transaction_amount,
    t.avg_transaction_amount,
    l.loan_amount_gbp,
    l.interest_rate_percent,
    l.loan_status,
    comp.total_complaints,
    comp.avg_resolution_days
FROM customers c
LEFT JOIN transactions_summary t
    ON c.customer_id = t.customer_id
LEFT JOIN loans l
    ON c.customer_id = l.customer_id
LEFT JOIN complaints_summary comp
    ON c.customer_id = comp.customer_id;

/* The final_dataset table now contains a consolidated view per customer,
      ready for Python EDA and modeling. */
