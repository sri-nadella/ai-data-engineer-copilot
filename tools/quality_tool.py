import pandas as pd
from database.db import engine

def check_quality(table_name):
    df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

    total_rows = len(df)
    nulls = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    return {
        "rows": total_rows,
        "nulls": nulls,
        "duplicates": duplicates
    }