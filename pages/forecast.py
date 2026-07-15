import streamlit as st
import plotly.express as px

from services.forecast_service import ForecastService


def show_forecast():

    st.title("📈 Demand Forecasting")

    products = [
        "Oreo Biscuit",
        "Premium Dates",
        "KitKat"
    ]

    product = st.selectbox(
        "Select Product",
        products
    )

    forecast = ForecastService.forecast_product(product)

    if forecast is None:

        st.warning("Not enough data.")

        return

    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title=f"Demand Forecast - {product}"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.dataframe(
        forecast.round(2),
        width="stretch"
    )