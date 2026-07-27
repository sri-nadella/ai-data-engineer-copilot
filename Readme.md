# AI Data Engineer Copilot (MCP)

An MCP (Model Context Protocol) server that exposes data engineering tools 
over a 540,000-row e-commerce dataset, enabling AI assistants to query, 
inspect, and analyze retail data through natural language.

## Tools Exposed

| Tool | Description | Input |
|------|-------------|-------|
| `schema` | Returns column names and data types | `table_name` |
| `quality` | Returns row count, null count, duplicate count | `table_name` |
| `revenue` | Returns top 10 customers by revenue | none |
| `lineage` | Returns data layer documentation | none |

## Dataset

Online Retail dataset — 541,909 rows, 8 columns:
`InvoiceNo`, `StockCode`, `Description`, `Quantity`, 
`InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

## Tech Stack

- Python 3.14
- FastMCP (MCP server framework)
- SQLite + SQLAlchemy
- Pandas

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/ai-data-engineer-copilot.git
cd ai-data-engineer-copilot
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
pip install "mcp[cli]"
```

**4. Download the dataset**

Download the Online Retail dataset from UCI ML Repository and save as `data/data.csv`

**5. Initialize the database**
```bash
python database/init_db.py
```

**6. Run the MCP server**
```bash
$env:PYTHONIOENCODING="utf-8"
mcp dev server.py
```

**7. Test via MCP Inspector**

Open the URL printed in the terminal, set Command=`python`, 
Arguments=`server.py`, click Connect, then List Tools.

## Project Structure

```
ai-data-engineer-copilot/
├── data/
│   └── data.csv
├── database/
│   ├── db.py
│   └── init_db.py
├── tools/
│   ├── schema_tool.py
│   ├── quality_tool.py
│   ├── revenue_tool.py
│   └── lineage_tool.py
├── server.py
├── test.py
├── requirements.txt
└── README.md
```