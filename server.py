from mcp.server.fastmcp import FastMCP

from tools.schema_tool import get_schema
from tools.quality_tool import check_quality
from tools.revenue_tool import top_customers
from tools.lineage_tool import get_lineage

mcp = FastMCP("RetailAnalyticsCopilot")

@mcp.tool()
def schema(table_name: str):
    return get_schema(table_name)

@mcp.tool()
def quality(table_name: str):
    return check_quality(table_name)

@mcp.tool()
def revenue():
    return top_customers()

@mcp.tool()
def lineage():
    return get_lineage()

if __name__ == "__main__":
    mcp.run()