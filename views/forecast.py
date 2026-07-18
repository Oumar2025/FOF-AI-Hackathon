import streamlit as st
import plotly.express as px
import pandas as pd

from services.forecast_service import ForecastService
from services.product_service import ProductService
from components.header import show_header


def show_forecast():

    # ======================================================
    # Header
    # ======================================================

    show_header(
        "📈 Demand Forecast",
        "Predict future inventory demand using AI."
    )

    # ======================================================
    # Executive Ranking
    # ======================================================

    st.markdown("---")
    st.subheader("📊 Executive Demand Ranking")

    st.caption(
        "Products ranked by expected demand to support import planning."
    )

    ranking = ForecastService.forecast_all_products()

    if len(ranking) == 0:

        st.warning("No forecast data available.")

        return

    ranking_df = pd.DataFrame(ranking)

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

    # ======================================================
    # Product Selection
    # ======================================================

    st.markdown("---")
    st.subheader("📦 Product Analysis")

    products = ProductService.get_product_names()

    product = st.selectbox(

        "Select Product",

        products

    )

    forecast = ForecastService.forecast_product(product)

    if forecast is None:

        st.warning("Not enough historical data.")

        return

    # ======================================================
    # Forecast Chart
    # ======================================================

    st.markdown("---")
    st.subheader("📈 Forecast Trend")

    fig = px.line(

        forecast,

        x="ds",

        y="yhat",

        title=f"Demand Forecast - {product}",

        markers=True

    )

    fig.update_layout(

        xaxis_title="Date",

        yaxis_title="Expected Demand",

        template="plotly_dark"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ======================================================
    # Forecast Summary
    # ======================================================

    st.markdown("---")
    st.subheader("📋 Forecast Summary")

    latest = forecast.iloc[-1]

    expected = round(latest["yhat"])

    lower = round(latest["yhat_lower"])

    upper = round(latest["yhat_upper"])

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "Expected Demand",

        f"{expected}"

    )

    col2.metric(

        "Lower Estimate",

        f"{lower}"

    )

    col3.metric(

        "Upper Estimate",

        f"{upper}"

    )

    # ======================================================
    # AI Business Interpretation
    # ======================================================

    st.markdown("---")
    st.subheader("🧠 AI Business Interpretation")

    current_stock = next(
        (
            item["Current Stock"]
            for item in ranking
            if item["Product"] == product
        ),
        0
    )

    recommendation = next(
        (
            item["Recommendation"]
            for item in ranking
            if item["Product"] == product
        ),
        "Maintain Stock"
    )

    seasonal_event = next(
        (
            item["Seasonal Event"]
            for item in ranking
            if item["Product"] == product
        ),
        "-"
    )

    if expected > current_stock:

        st.error(
            f"""
The expected demand for **{product}** is **{expected} units** while
current inventory is only **{current_stock} units**.

Immediate purchasing is recommended to reduce the risk of stock shortages.
"""
        )

    elif expected >= current_stock * 0.6:

        st.warning(
            f"""
Demand is expected to remain stable.

Current inventory appears adequate, but inventory levels should be monitored
closely over the coming weeks.
"""
        )

    else:

        st.success(
            f"""
Current inventory comfortably covers the expected demand.

No immediate purchasing action is required.
"""
        )

    # ======================================================
    # Recommended Import Plan
    # ======================================================

    st.markdown("---")
    st.subheader("📦 Recommended Import Plan")

    import_qty = max(expected - current_stock, 0)

    col1, col2 = st.columns(2)

    col1.metric(
        "Recommended Import",
        f"{import_qty} Units"
    )

    col2.metric(
        "Current Stock",
        f"{current_stock} Units"
    )

    st.info(
        f"""
**Recommendation:** {recommendation}

**Seasonal Event:** {seasonal_event}

This recommendation combines historical sales forecasting with seasonal
business trends to support inventory planning.
"""
    )

    # ======================================================
    # Forecast Details
    # ======================================================

    st.markdown("---")
    st.subheader("📄 Forecast Details")

    forecast_table = forecast.copy()

    forecast_table = forecast_table.rename(
        columns={
            "ds": "Date",
            "yhat": "Forecast",
            "yhat_lower": "Lower Bound",
            "yhat_upper": "Upper Bound"
        }
    )

    forecast_table["Forecast"] = (
        forecast_table["Forecast"]
        .round()
        .astype(int)
    )

    forecast_table["Lower Bound"] = (
        forecast_table["Lower Bound"]
        .round()
        .astype(int)
    )

    forecast_table["Upper Bound"] = (
        forecast_table["Upper Bound"]
        .round()
        .astype(int)
    )

    st.dataframe(
        forecast_table,
        use_container_width=True,
        hide_index=True
    )

    # ======================================================
    # Executive Recommendation
    # ======================================================

    st.markdown("---")
    st.subheader("🎯 Executive Recommendation")

    if recommendation == "Increase Import":

        st.error("""
### Priority: HIGH

Increase purchase orders immediately.

Expected demand exceeds available inventory.
Failure to replenish stock may result in lost sales.
""")

    elif recommendation == "Maintain Stock":

        st.warning("""
### Priority: MEDIUM

Current inventory is sufficient.

Continue monitoring sales and review demand next month.
""")

    else:

        st.success("""
### Priority: LOW

Inventory levels are healthy.

No immediate purchasing action is required.
Continue normal inventory monitoring.
""")







