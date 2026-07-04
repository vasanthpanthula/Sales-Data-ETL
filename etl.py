import pandas as pd
import mysql.connector

# Step 1: Read CSV
df = pd.read_csv("sales.csv")

# Step 2: Clean Data
df = df.drop_duplicates()
df = df.dropna()

# Step 3: Convert Date
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="mixed",
    dayfirst=True
)

# Step 4: Create Total Amount
df["total_amount"] = df["quantity"] * df["price"]

# Step 5: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="salesdb"
)

cursor = connection.cursor()

print("Connected Successfully!")


# Remove old data
cursor.execute("DELETE FROM sales")

# Step 6: Insert data into MySQL


query = """
INSERT INTO sales
(order_id, product, category, quantity, price, order_date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for index, row in df.iterrows():
    cursor.execute(query, (
        int(row["order_id"]),
        row["product"],
        row["category"],
        int(row["quantity"]),
        float(row["price"]),
        row["order_date"].date()
    ))

connection.commit()

print(f"{len(df)} rows inserted successfully!")


# Close the connection
cursor.close()
connection.close()

print("Connection closed successfully!")