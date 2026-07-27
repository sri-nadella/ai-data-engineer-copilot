from sqlalchemy import text
from database.db import engine

def top_customers():
    query = """
    SELECT
        CustomerID,
        SUM(Quantity * UnitPrice) as revenue
    FROM retail
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
    ORDER BY revenue DESC
    LIMIT 10
    """

    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()

    result = []
    for row in rows:
        result.append({
            "CustomerID": row[0],
            "Revenue": round(row[1], 2)
        })

    return result