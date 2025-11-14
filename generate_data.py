import csv
import random
from faker import Faker

fake = Faker()

# Generate Customers data
with open('customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'email'])
    for i in range(1, 101):
        writer.writerow([i, fake.name(), fake.email()])

# Generate Products data
with open('products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'title', 'price'])
    for i in range(1, 51):
        writer.writerow([i, fake.word().title(), round(fake.pyfloat(right_digits=2, min_value=10, max_value=500), 2)])

# Generate Orders data
with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'customer_id', 'order_date'])
    for i in range(1, 201):
        writer.writerow([i, random.randint(1, 100), fake.date_this_year()])

# Generate Order Items data
with open('order_items.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'order_id', 'product_id', 'quantity'])
    for i in range(1, 401):
        writer.writerow([i, random.randint(1, 200), random.randint(1, 50), random.randint(1, 5)])
