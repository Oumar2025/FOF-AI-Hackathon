import sqlite3
from models.product import Product

from config.settings import DATABASE_NAME


class ProductService:

    @staticmethod
    def add_product(product):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO products(
            product_name,
            category,
            brand,
            supplier_country,
            destination_country,
            quantity,
            unit,
            cost_price,
            selling_price,
            manufacture_date,
            expiry_date,
            warehouse,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            product.product_name,
            product.category,
            product.brand,
            product.supplier_country,
            product.destination_country,
            product.quantity,
            product.unit,
            product.cost_price,
            product.selling_price,
            product.manufacture_date,
            product.expiry_date,
            product.warehouse,
            product.status

        ))

        conn.commit()
        conn.close()

        return True
    
    @staticmethod
    def get_all_products():

        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM products
            ORDER BY product_id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
    @staticmethod
    def get_dashboard_statistics():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Total Products
        cursor.execute("SELECT COUNT(*) FROM products")
        total_products = cursor.fetchone()[0]

        # Low Stock (Quantity أقل من 100)
        cursor.execute("""
            SELECT COUNT(*)
            FROM products
            WHERE quantity < 100
        """)
        low_stock = cursor.fetchone()[0]

        # Expiring Soon (currently placeholder)
        expiring_soon = 0

        # Destination Countries
        cursor.execute("""
            SELECT COUNT(DISTINCT destination_country)
            FROM products
        """)
        countries = cursor.fetchone()[0]

        conn.close()

        return {
            "total_products": total_products,
            "low_stock": low_stock,
            "expiring_soon": expiring_soon,
            "countries": countries
        }
    
    @staticmethod
    def get_chart_data():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Category Chart
        cursor.execute("""
            SELECT category, COUNT(*)
            FROM products
            GROUP BY category
        """)
        category_data = cursor.fetchall()

        # Supplier Chart
        cursor.execute("""
            SELECT supplier_country, COUNT(*)
            FROM products
            GROUP BY supplier_country
        """)
        supplier_data = cursor.fetchall()

        # Destination Chart
        cursor.execute("""
            SELECT destination_country, COUNT(*)
            FROM products
            GROUP BY destination_country
        """)
        destination_data = cursor.fetchall()

        conn.close()

        return category_data, supplier_data, destination_data
    
    @staticmethod
    def get_product_by_id(product_id):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM products
            WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        conn.close()

        return product
    
    @staticmethod
    def delete_product(product_id):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (product_id,))

        conn.commit()
        conn.close()

        return True
    
    @staticmethod
    def update_product(product):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE products
            SET
                product_name=?,
                category=?,
                brand=?,
                supplier_country=?,
                destination_country=?,
                quantity=?,
                unit=?,
                cost_price=?,
                selling_price=?,
                manufacture_date=?,
                expiry_date=?,
                warehouse=?,
                status=?
            WHERE product_id=?
        """, (

            product.product_name,
            product.category,
            product.brand,
            product.supplier_country,
            product.destination_country,
            product.quantity,
            product.unit,
            product.cost_price,
            product.selling_price,
            product.manufacture_date,
            product.expiry_date,
            product.warehouse,
            product.status,
            product.product_id

        ))

        conn.commit()
        conn.close()

        return True
    
    @staticmethod
    def get_expiring_products(days=90):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM products
        """)

        products = cursor.fetchall()

        conn.close()

        from datetime import datetime, timedelta

        today = datetime.today()

        expiring = []

        for product in products:

            expiry = datetime.strptime(
                product[11],
                "%Y-%m-%d"
            )

            days_left = (expiry - today).days

            if days_left <= days:

                expiring.append(
                    (
                        product,
                        days_left
                    )
                )

        return expiring
    
    @staticmethod
    def get_product_names():

        products = ProductService.get_all_products()

        return [p[1] for p in products]


    @staticmethod
    def seed_demo_products():

        import sqlite3
        from config.settings import DATABASE_NAME

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Don't insert again if products already exist
        cursor.execute("SELECT COUNT(*) FROM products")

        if cursor.fetchone()[0] > 0:
            conn.close()
            return

        demo_products = [

            (
                "Koka",
                "Noodles",
                "Koka",
                "Singapore",
                "Mali",
                500,
                "Boxes",
                8.50,
                12.00,
                "2026-01-01",
                "2027-01-01",
                "Warehouse A",
                "Available"
            ),

            (
                "TOP",
                "Biscuit",
                "TOP",
                "Turkey",
                "Mali",
                350,
                "Cartons",
                10.00,
                15.00,
                "2026-02-01",
                "2027-02-01",
                "Warehouse A",
                "Available"
            ),

            (
                "LAZTO",
                "Candy",
                "LAZTO",
                "Turkey",
                "Burkina Faso",
                450,
                "Boxes",
                6.50,
                10.00,
                "2026-03-01",
                "2027-03-01",
                "Warehouse B",
                "Available"
            ),

            (
                "Romma",
                "Chocolate",
                "Romma",
                "Turkey",
                "Angola",
                280,
                "Cartons",
                14.00,
                20.00,
                "2026-02-15",
                "2027-02-15",
                "Warehouse A",
                "Available"
            ),

            (
                "Oreo Biscuit",
                "Biscuit",
                "Oreo",
                "Indonesia",
                "Mali",
                600,
                "Boxes",
                7.00,
                11.00,
                "2026-01-10",
                "2027-01-10",
                "Warehouse C",
                "Available"
            ),

            (
                "BCSO",
                "Chocolate",
                "BCSO",
                "Turkey",
                "Côte d'Ivoire",
                320,
                "Cartons",
                12.00,
                17.50,
                "2026-02-20",
                "2027-02-20",
                "Warehouse B",
                "Available"
            )

        ]

        cursor.executemany("""
            INSERT INTO products(
                product_name,
                category,
                brand,
                supplier_country,
                destination_country,
                quantity,
                unit,
                cost_price,
                selling_price,
                manufacture_date,
                expiry_date,
                warehouse,
                status
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, demo_products)

        conn.commit()
        conn.close()    