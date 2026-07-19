import sqlite3
from config.settings import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

tables = [
    "products",
    "sales_history",
    "seasonal_events"
]

print("=" * 50)
print("DATABASE VERIFICATION")
print("=" * 50)

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table:<20}: {count}")

conn.close()