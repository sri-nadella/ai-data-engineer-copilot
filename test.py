from tools.schema_tool import get_schema
from tools.quality_tool import check_quality
from tools.revenue_tool import top_customers
from tools.lineage_tool import get_lineage

print("=== SCHEMA ===")
print(get_schema("retail"))

print("\n=== QUALITY ===")
print(check_quality("retail"))

print("\n=== TOP CUSTOMERS ===")
print(top_customers())

print("\n=== LINEAGE ===")
print(get_lineage())