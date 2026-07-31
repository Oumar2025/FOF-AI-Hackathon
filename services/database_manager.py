import sqlite3

from narwhals.selectors import datetime
from config.settings import DATABASE_NAME


class DatabaseManager:

    @staticmethod
    def initialize_database():

        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.cursor()
        

        cursor.execute("PRAGMA foreign_keys = ON")

        # ==================================================
        # PRODUCTS
        # ==================================================

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS products(

            product_id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_name TEXT NOT NULL,

            category TEXT NOT NULL,

            brand TEXT,

            supplier_country TEXT,

            destination_country TEXT,

            quantity INTEGER,

            unit TEXT,

            cost_price REAL,

            selling_price REAL,

            manufacture_date TEXT,

            expiry_date TEXT,

            warehouse TEXT,

            status TEXT

        )

        """)

        # ==================================================
        # SALES HISTORY
        # ==================================================

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS sales_history(

            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_id INTEGER NOT NULL,

            country TEXT NOT NULL,

            sale_date TEXT NOT NULL,

            units_sold INTEGER NOT NULL,

           

            FOREIGN KEY(product_id)
                REFERENCES products(product_id)
                ON DELETE CASCADE

        )

        """)

        # ==================================================
        # SEASONAL EVENTS
        # ==================================================

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS seasonal_events(

            event_id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT NOT NULL,

            event TEXT NOT NULL,

            start_date TEXT NOT NULL,

            end_date TEXT NOT NULL,

            demand_multiplier REAL NOT NULL

        )

        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alert_history (

            alert_id INTEGER PRIMARY KEY AUTOINCREMENT,

            product_id INTEGER NOT NULL,

            alert_level INTEGER NOT NULL,

            sent_at TEXT NOT NULL,

            acknowledged INTEGER DEFAULT 0,

            muted INTEGER DEFAULT 0,

            resolved INTEGER DEFAULT 0,

            

            FOREIGN KEY(product_id)
                REFERENCES products(product_id)
                ON DELETE CASCADE

        )
        """)


        

        conn.commit()

        conn.close()

        print("Database created successfully.")