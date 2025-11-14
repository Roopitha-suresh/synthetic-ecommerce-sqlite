# Synthetic Ecommerce SQLite

## Overview
This repo demonstrates a tiny synthetic data pipeline for an ecommerce-style SQLite database. It includes a generator for customer and product CSV files, a loader that ingests the CSVs into `ecommerce.db`, and a sample analytics query script you can adapt for reporting or demos.

## Repository layout
- `generate_data.py` – builds `customers.csv` (100 fake shoppers) and `products.csv` (50 fake SKUs) using the Faker library.
- `import_to_sqlite.py` – creates `customers` and `products` tables inside `ecommerce.db` (in the repo root) and bulk-loads the generated CSV files.
- `query_db.py` – example query that ranks the top 10 customers by spend, assuming `orders` and `order_items` tables exist. Use it as a template after you add those tables/data.
- `customers.csv`, `products.csv` – artifacts produced by the generator script.

## Prerequisites
- Python 3.9+ (any modern CPython works)
- `pip install faker`
- SQLite command-line tools (optional, for manual inspection)

## Usage
1. **Install dependencies**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate        # PowerShell
   pip install faker
   ```
2. **Generate synthetic CSVs**
   ```bash
   python generate_data.py
   ```
3. **Import into SQLite**
   ```bash
   python import_to_sqlite.py
   ```
   This creates or updates `ecommerce.db` in the repo directory.
4. **Run analytics queries**
   - Use the SQLite CLI, e.g. `sqlite3 ecommerce.db "SELECT * FROM customers LIMIT 5;"`
   - Or adapt `query_db.py`. Before running it, make sure you have created and populated `orders` and `order_items` tables that reference `customers` and `products`.

## Database schema
Current tables managed by the scripts:
- `customers(id INTEGER, name TEXT, email TEXT)`
- `products(id INTEGER, title TEXT, price REAL)`

Feel free to extend the schema with `orders` and `order_items` to match the joins in `query_db.py`.

## Extending the project
- Add more Faker-powered datasets (orders, order_items) and import routines similar to `import_to_sqlite.py`.
- Create indexes or views inside SQLite to speed up specific demos.
- Wire the database into a BI or dashboard tool for richer storytelling.

## Troubleshooting
- Delete `customers.csv`, `products.csv`, or `ecommerce.db` if you want a clean slate and re-run the scripts.
- If `query_db.py` raises `no such table: orders`, create those tables first or adjust the query to match the data you have loaded.
