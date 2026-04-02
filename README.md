# MySQL Banking Database

- Course: CMP2806M – Scalable Database Systems
- Institution: University of Lincoln
- Grade Received: 80%
- Tech: MySQL, XAMPP Apache phpMyAdmin, Python

# Overview
A normalised banking database supporting customer accounts, transactions, and loan management. Designed to 2NF with referential integrity constraints.

# Schema
- **Customers** – Personal details (100 records)
- **Account** – Sort code, account number, opening balance (>£50)
- **Bank** – Junction table (customers ↔ accounts)
- **Transactions** – 1 month of history (10,000+ records via Python script)
- **Loans** – Payment schedules with monthly due dates

## Key Queries
| ID | Description |
|----|-------------|
| 4.1 | Customers with loan payments due in the first 7 days |
| 4.2 | Transactions from last 5 days (dynamic) |
| 4.3 | Customers with balance > £5000 (using CTE) |
| 4.4 | Bank-wide total outstandings |
