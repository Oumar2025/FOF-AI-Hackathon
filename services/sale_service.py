import sqlite3
from config.settings import DATABASE_NAME


class SaleService:

    @staticmethod
    def add_sale(product_id, country, sale_date, units_sold):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO sales_history
            (product_id, country, sale_date, units_sold)
            VALUES (?, ?, ?, ?)
        """, (
            product_id,
            country,
            sale_date,
            units_sold
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_sales():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sale_id,
                product_id,
                country,
                sale_date,
                units_sold
            FROM sales_history
            ORDER BY sale_date
        """)

        sales = cursor.fetchall()

        conn.close()

        return sales

    @staticmethod
    def delete_all_sales():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM sales_history")

        conn.commit()
        conn.close()