import sqlite3

DATABASE_NAME = "data/inventory.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        
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

    conn.commit()
    conn.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()