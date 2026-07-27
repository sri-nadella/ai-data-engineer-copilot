def get_lineage():
    return {
        "raw_layer": "data.csv",
        "bronze_layer": "retail table",
        "silver_layer": "cleaned retail records",
        "gold_layer": "customer revenue metrics",
        "dashboard": "Power BI Sales Dashboard"
    }