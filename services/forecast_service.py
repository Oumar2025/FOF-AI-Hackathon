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