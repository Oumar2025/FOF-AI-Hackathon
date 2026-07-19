import pandas as pd
from datetime import datetime
from prophet import Prophet


class ForecastService:

    @staticmethod
    def forecast_product(product_name):

        import sqlite3
        from config.settings import DATABASE_NAME

        conn = sqlite3.connect(DATABASE_NAME)

        query = """
            SELECT
                sh.sale_date,
                sh.units_sold
            FROM sales_history sh
            JOIN products p
                ON sh.product_id = p.product_id
            WHERE p.product_name = ?
            ORDER BY sh.sale_date
        """

        df = pd.read_sql_query(
            query,
            conn,
            params=(product_name,)
        )

        conn.close()

        if len(df) < 2:
            return None

        df = df.rename(
            columns={
                "sale_date": "ds",
                "units_sold": "y"
            }
        )

        df["ds"] = pd.to_datetime(df["ds"])

        model = Prophet()

        model.fit(df)

        future = model.make_future_dataframe(
            periods=3,
            freq="ME"
        )

        forecast = model.predict(future)

        return forecast[
            [
                "ds",
                "yhat",
                "yhat_lower",
                "yhat_upper"
            ]
        ]
    
    @staticmethod
    def get_next_month_prediction(product_name):

        forecast = ForecastService.forecast_product(product_name)

        if forecast is None:
            return None

        next_month = forecast.iloc[-1]

        return round(next_month["yhat"])    

    @staticmethod
    def seasonal_multiplier(category):

        import sqlite3
        from config.settings import DATABASE_NAME

        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                event,
                start_date,
                end_date,
                demand_multiplier
            FROM seasonal_events
            WHERE category = ?
        """, (category,))

        rows = cursor.fetchall()

        conn.close()

        today = datetime.today().date()

        for row in rows:

            event = row[0]
            start = datetime.strptime(row[1], "%Y-%m-%d").date()
            end = datetime.strptime(row[2], "%Y-%m-%d").date()
            multiplier = row[3]

            if start <= today <= end:
                return multiplier, event

        return 1.0, None    
    
    @staticmethod
    def forecast_all_products():

        from services.product_service import ProductService

        ranking = []

        products = ProductService.get_all_products()

        for product in products:

            product_name = product[1]      # Product Name
            category = product[2]          # Category
            quantity = product[6]          # Current Stock

            prediction = ForecastService.get_next_month_prediction(product_name)

            if prediction is None:
                continue

            multiplier, event = ForecastService.seasonal_multiplier(category)

            expected_demand = round(prediction * multiplier)

            if expected_demand > quantity:

                recommendation = "Increase Import"

            elif expected_demand < quantity * 0.6:

                recommendation = "Monitor"

            else:

                recommendation = "Maintain Stock"

            ranking.append({

                "Product": product_name,
                "Current Stock": quantity,
                "Expected Demand": expected_demand,
                "Recommendation": recommendation,
                "Seasonal Event": event if event else "-"

            })

        ranking = sorted(

            ranking,

            key=lambda x: x["Expected Demand"],

            reverse=True

        )

        return ranking