from sqlalchemy import inspect
from database.db import engine

def get_schema(table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)

    result = []
    for column in columns:
        result.append({
            "column": column["name"],
            "type": str(column["type"])
        })

    return result