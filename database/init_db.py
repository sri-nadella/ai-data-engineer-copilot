import pandas as pd
import sqlite3

print("Loading CSV...")

df = pd.read_csv(
    "data/data.csv",
    encoding="latin1"
)

print("\nColumns:")
print(df.columns.tolist())

print("\nNumber of rows:")
print(len(df))

conn = sqlite3.connect("retail.db")

df.to_sql(
    "retail",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nDatabase Created Successfully!")
