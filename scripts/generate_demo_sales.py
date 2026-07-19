import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)


import sqlite3
import random

from config.settings import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

# Remove previous demo sales
cursor.execute("DELETE FROM sales_history")

# Get all products
cursor.execute("""
SELECT
    product_id,
    product_name,
    category,
    destination_country
FROM products
""")

products = cursor.fetchall()

months = [

    "2026-01-01",
    "2026-02-01",
    "2026-03-01",
    "2026-04-01",
    "2026-05-01",
    "2026-06-01"

]

for product in products:

    product_id = product[0]
    category = product[2]
    country = product[3]

    # Base demand by category

    if category == "Dates":

        base = 350

    elif category == "Chocolate":

        base = 220

    elif category == "Biscuit":

        base = 180

    elif category == "Candy":

        base = 160

    else:

        base = 150

    demand = base

    for month in months:

        demand += random.randint(10, 40)

        cursor.execute("""

            INSERT INTO sales_history(

                product_id,
                country,
                sale_date,
                units_sold

            )

            VALUES(?,?,?,?)

        """, (

            product_id,
            country,
            month,
            demand

        ))

conn.commit()
conn.close()

print("✅ Demo sales history generated successfully.")