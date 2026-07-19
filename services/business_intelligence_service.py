import sqlite3
from config.settings import DATABASE_NAME


class BusinessIntelligenceService:

    @staticmethod
    def get_inventory_summary():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Total Products
        cursor.execute("""
            SELECT COUNT(*)
            FROM products
        """)
        total_products = cursor.fetchone()[0]

        # Total Units
        cursor.execute("""
            SELECT SUM(quantity)
            FROM products
        """)
        total_units = cursor.fetchone()[0] or 0

        # Inventory Value
        cursor.execute("""
            SELECT SUM(quantity * cost_price)
            FROM products
        """)
        inventory_value = cursor.fetchone()[0] or 0

        # Expected Revenue
        cursor.execute("""
            SELECT SUM(quantity * selling_price)
            FROM products
        """)
        expected_revenue = cursor.fetchone()[0] or 0

        expected_profit = expected_revenue - inventory_value

        conn.close()

        return {

            "total_products": total_products,

            "total_units": total_units,

            "inventory_value": round(inventory_value, 2),

            "expected_revenue": round(expected_revenue, 2),

            "expected_profit": round(expected_profit, 2)

        }


    @staticmethod
    def get_inventory_analysis():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                product_name,
                quantity,
                unit,
                warehouse
            FROM products
            ORDER BY quantity ASC
        """)

        products = cursor.fetchall()

        conn.close()

        analysis = {
            "low_stock": [],
            "healthy_stock": [],
            "overstock": []
        }

        for product in products:

            name, qty, unit, warehouse = product

            item = {
                "product": name,
                "quantity": qty,
                "unit": unit,
                "warehouse": warehouse
            }

            if qty < 200:
                analysis["low_stock"].append(item)

            elif qty > 500:
                analysis["overstock"].append(item)

            else:
                analysis["healthy_stock"].append(item)

        return analysis    
    
    @staticmethod
    def get_sales_summary():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.product_name,
                SUM(sh.units_sold) AS total_units
            FROM sales_history sh
            JOIN products p
                ON sh.product_id = p.product_id
            GROUP BY p.product_name
            ORDER BY total_units DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        if not rows:
            return {
                "top_selling": [],
                "total_units_sold": 0
            }

        total_units = sum(row[1] for row in rows)

        top_selling = [
            {
                "product": row[0],
                "units_sold": row[1]
            }
            for row in rows[:5]
        ]

        return {
            "top_selling": top_selling,
            "total_units_sold": total_units
        }
    

    @staticmethod
    def get_expiry_analysis(days=30):

        import sqlite3
        from datetime import datetime, timedelta
        from config.settings import DATABASE_NAME

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                product_name,
                quantity,
                expiry_date,
                warehouse
            FROM products
            ORDER BY expiry_date
        """)

        rows = cursor.fetchall()
        conn.close()

        today = datetime.today().date()
        limit = today + timedelta(days=days)

        expiring = []

        for row in rows:

            product, quantity, expiry_date, warehouse = row

            expiry = datetime.strptime(
                expiry_date,
                "%Y-%m-%d"
            ).date()

            if today <= expiry <= limit:

                expiring.append({

                    "product": product,
                    "quantity": quantity,
                    "expiry_date": expiry_date,
                    "warehouse": warehouse,
                    "days_remaining": (expiry - today).days

                })

        return expiring


    @staticmethod
    def generate_business_report():

        return {

            "inventory_summary":
                BusinessIntelligenceService.get_inventory_summary(),

            "inventory_analysis":
                BusinessIntelligenceService.get_inventory_analysis(),

            "sales_summary":
                BusinessIntelligenceService.get_sales_summary(),

            "expiry_analysis":
                BusinessIntelligenceService.get_expiry_analysis(),

            "forecast_summary":
                BusinessIntelligenceService.get_forecast_summary()

        }  


    @staticmethod
    def get_forecast_summary():

        from services.product_service import ProductService
        from services.forecast_service import ForecastService

        products = ProductService.get_all_products()

        forecasts = []

        for product in products:

            name = product[1]
            current_stock = product[6]

            prediction = ForecastService.get_next_month_prediction(name)

            if prediction is None:
                continue

            multiplier, event = ForecastService.seasonal_multiplier(product[2])

            adjusted_prediction = round(prediction * multiplier)

            # Keep approximately two months of forecast as a buffer
            safety_stock = round(adjusted_prediction * 2)

            reorder_point = adjusted_prediction + safety_stock

            recommended_import = max(
                reorder_point - current_stock,
                0
            )

            forecasts.append({

                "product": name,

                "current_stock": current_stock,

                "predicted_demand": adjusted_prediction,

                "safety_stock": safety_stock,

                "reorder_point": reorder_point,

                "recommended_import": recommended_import,

                "season": event if event else "Normal"

            })

        forecasts.sort(
            key=lambda x: x["predicted_demand"],
            reverse=True
        )

        return forecasts    