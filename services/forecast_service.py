import pandas as pd
from datetime import datetime
from prophet import Prophet


class ForecastService:

    @staticmethod
    def forecast_product(product_name):

        df = pd.read_csv("data/sales_history.csv")

        df = df[df["Product"] == product_name]

        if len(df) < 2:
            return None

        df = df.rename(
            columns={
                "Date": "ds",
                "UnitsSold": "y"
            }
        )

        model = Prophet()

        model.fit(df[["ds", "y"]])

        future = model.make_future_dataframe(
            periods=3,
            freq="ME"
        )

        forecast = model.predict(future)

        return forecast[
            ["ds", "yhat", "yhat_lower", "yhat_upper"]
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

        seasons = pd.read_csv(
            "data/seasonal_events.csv"
        )

        today = datetime.today()

        for _, row in seasons.iterrows():

            start = datetime.strptime(
                row["StartDate"],
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                row["EndDate"],
                "%Y-%m-%d"
            )

            if (
                row["Category"] == category
                and start <= today <= end
            ):

                return row["DemandMultiplier"], row["Event"]

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