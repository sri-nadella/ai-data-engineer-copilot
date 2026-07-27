"""
Derives a normalized practice schema (customers, products, orders, order_items)
from the flat `retail` table, for hands-on SQL learning (JOINs, FKs, etc).

Run this AFTER init_db.py has already created retail.db / the retail table.
"""

import sqlite3
import pandas as pd
from database.db import engine

print("Reading retail table...")
df = pd.read_sql("SELECT * FROM retail", engine)

# --- customers: one row per known CustomerID ---
customers_df = (
    df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["Country"]
    .agg(lambda s: s.mode().iat[0])
    .reset_index()
)
customers_df["CustomerID"] = customers_df["CustomerID"].astype(int)

# --- products: one row per StockCode ---
products_df = (
    df.dropna(subset=["StockCode"])
    .groupby("StockCode")["Description"]
    .agg(lambda s: s.mode().iat[0] if not s.mode().empty else None)
    .reset_index()
)

# --- orders: one row per InvoiceNo ---
orders_df = (
    df.groupby("InvoiceNo")
    .agg(CustomerID=("CustomerID", "first"), InvoiceDate=("InvoiceDate", "first"))
    .reset_index()
)
orders_df["CustomerID"] = orders_df["CustomerID"].astype("Int64")
orders_df["CustomerID"] = orders_df["CustomerID"].where(orders_df["CustomerID"].notna(), None)

# --- order_items: one row per original line item ---
order_items_df = df[["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]].reset_index(drop=True)

print(f"customers: {len(customers_df)}")
print(f"products: {len(products_df)}")
print(f"orders: {len(orders_df)}")
print(f"order_items: {len(order_items_df)}")

conn = sqlite3.connect("retail.db")
cur = conn.cursor()

cur.executescript(
    """
    DROP TABLE IF EXISTS order_items;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS customers;

    CREATE TABLE customers (
        CustomerID INTEGER PRIMARY KEY,
        Country TEXT
    );

    CREATE TABLE products (
        StockCode TEXT PRIMARY KEY,
        Description TEXT
    );

    CREATE TABLE orders (
        InvoiceNo TEXT PRIMARY KEY,
        CustomerID INTEGER,
        InvoiceDate TEXT,
        FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
    );

    CREATE TABLE order_items (
        OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        InvoiceNo TEXT,
        StockCode TEXT,
        Quantity INTEGER,
        UnitPrice REAL,
        FOREIGN KEY (InvoiceNo) REFERENCES orders(InvoiceNo),
        FOREIGN KEY (StockCode) REFERENCES products(StockCode)
    );
    """
)
conn.commit()

customers_df.to_sql("customers", conn, if_exists="append", index=False)
products_df.to_sql("products", conn, if_exists="append", index=False)
orders_df.to_sql("orders", conn, if_exists="append", index=False)
order_items_df.to_sql("order_items", conn, if_exists="append", index=False)

conn.close()
print("\nPractice schema created: customers, products, orders, order_items")
