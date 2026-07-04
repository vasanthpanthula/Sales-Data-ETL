# Sales Data ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that extracts sales data from CSV files, cleans and transforms it using Pandas, and loads it into MySQL for analytics and reporting.


# Project Overview

This project demonstrates how a Data Engineer processes raw sales data into analytics-ready datasets.

The pipeline performs the following tasks:

- Extracts sales data from a CSV file
- Cleans and validates the dataset
- Removes duplicate and missing records
- Converts date columns into proper datetime format
- Creates derived metrics such as **total_amount**
- Loads the processed data into a MySQL database
- Generates business insights using SQL queries


# Technologies Used

- Python
- Pandas
- MySQL
- SQL
- mysql-connector-python
- Git
- GitHub
- VS Code


# ETL Workflow

```
Raw CSV File
      │
      ▼
Extract
(Read CSV using Pandas)
      │
      ▼
Transform
• Remove duplicates
• Remove missing values
• Convert dates
• Calculate total_amount
      │
      ▼
Load
(Store data into MySQL)
      │
      ▼
SQL Analytics
      │
      ▼
Business Reports
```


# Project Structure

```
Sales-Data-ETL/
│
├── etl.py
├── sales.csv
├── sales.xlsx
├── README.md
└── requirements.txt
```


# Features

- Read sales data from CSV files
- Data cleaning using Pandas
- Data validation
- Remove duplicate records
- Remove missing values
- Convert dates into datetime format
- Create calculated columns
- Load data into MySQL
- Generate analytics-ready datasets
- Execute SQL queries for reporting


# Data Transformation

The following transformations are performed:

- Remove duplicate records

```python
df = df.drop_duplicates()
```

- Remove missing values

```python
df = df.dropna()
```

- Convert date column

```python
df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", dayfirst=True)
```

- Create total sales amount

```python
df["total_amount"] = df["quantity"] * df["price"]
```


# MySQL Loading

The cleaned data is inserted into MySQL using **mysql-connector-python**.

Example:

```python
cursor.execute(query, values)
connection.commit()
```


# SQL Analysis

Example SQL queries used in this project:

### Total Sales

```sql
SELECT SUM(quantity * price)
FROM sales;
```

### Category-wise Sales

```sql
SELECT category,
SUM(quantity * price)
FROM sales
GROUP BY category;
```

### Average Product Price

```sql
SELECT AVG(price)
FROM sales;
```

### Total Products Sold

```sql
SELECT product,
SUM(quantity)
FROM sales
GROUP BY product;
```


# Real-Time Use Case

Imagine an e-commerce company like Amazon or Flipkart.

Every day thousands of orders are generated.

The ETL pipeline:

- Extracts daily sales data
- Cleans duplicate and invalid records
- Standardizes the data
- Loads the cleaned dataset into MySQL
- Generates reports for business teams
- Provides analytics-ready data for dashboards such as Power BI or Tableau


# How to Run

### Clone Repository

```bash
git clone https://github.com/vasanthpanthula/Sales-Data-ETL.git
```

### Install Required Libraries

```bash
pip install pandas
pip install mysql-connector-python
```

### Configure MySQL

Create a database named:

```sql
CREATE DATABASE salesdb;
```

Create the required table:

```sql
CREATE TABLE sales (
    order_id INT,
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE
);
```

Update your MySQL credentials in **etl.py**.

Run the project:

```bash
python etl.py
```


# Skills Demonstrated

- ETL Pipeline Development
- Python Programming
- Pandas
- Data Cleaning
- Data Transformation
- Data Validation
- SQL
- MySQL
- Database Connectivity
- Analytics
- Git
- GitHub


# Learning Outcomes

Through this project I learned:

- How ETL pipelines work
- Reading CSV files using Pandas
- Cleaning and transforming datasets
- Connecting Python with MySQL
- Loading processed data into databases
- Writing SQL queries for business reporting
- Managing projects using Git and GitHub


# Author

**Vasanth Panthula**

- GitHub: https://github.com/vasanthpanthula
- LinkedIn: https://www.linkedin.com/in/vasanth-panthula/


## If you found this project useful, consider giving it a Star on GitHub!