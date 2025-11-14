import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT c.id, c.name, SUM(oi.quantity * p.price) AS total_spent
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.id, c.name
    ORDER BY total_spent DESC
    LIMIT 10
''')

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
