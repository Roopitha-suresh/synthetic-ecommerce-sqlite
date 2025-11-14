import sqlite3
import csv

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables for everything
cursor.execute('CREATE TABLE IF NOT EXISTS customers (id INTEGER, name TEXT, email TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER, title TEXT, price REAL)')
cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER, customer_id INTEGER, order_date TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS order_items (id INTEGER, order_id INTEGER, product_id INTEGER, quantity INTEGER)')

# Import customers
with open('customers.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(row['id'], row['name'], row['email']) for row in dr]
cursor.executemany('INSERT INTO customers (id, name, email) VALUES (?, ?, ?);', to_db)

# Import products
with open('products.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(row['id'], row['title'], row['price']) for row in dr]
cursor.executemany('INSERT INTO products (id, title, price) VALUES (?, ?, ?);', to_db)

# Import orders
with open('orders.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(row['id'], row['customer_id'], row['order_date']) for row in dr]
cursor.executemany('INSERT INTO orders (id, customer_id, order_date) VALUES (?, ?, ?);', to_db)

# Import order_items
with open('order_items.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(row['id'], row['order_id'], row['product_id'], row['quantity']) for row in dr]
cursor.executemany('INSERT INTO order_items (id, order_id, product_id, quantity) VALUES (?, ?, ?, ?);', to_db)

conn.commit()
conn.close()
