
from PIL import report
import streamlit as st
import pandas as pd
import plotly.express as px

from services.product_service import ProductService
from services.ai_service import AIService



def show_dashboard():

    st.title("🤖 FOF-AI")

    st.subheader("AI Business Intelligence Assistant")
    st.subheader("🚨 Smart Business Alerts")

    if st.button("📧 Check & Send Alerts"):

        AIService.check_and_send_alerts()

        st.success("✅ Alert check completed successfully!")

    st.markdown("---")

    stats = ProductService.get_dashboard_statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📦 Products", stats["total_products"])
    col2.metric("⚠ Low Stock", stats["low_stock"])
    col3.metric("📅 Expiring Soon", stats["expiring_soon"])
    col4.metric("🌍 Countries", stats["countries"])

    st.markdown("---")

    st.subheader("📊 Business Analytics")

    category_data, supplier_data, destination_data = ProductService.get_chart_data()

    col1, col2 = st.columns(2)

    with col1:

        if category_data:

            category_df = pd.DataFrame(
                category_data,
                columns=["Category", "Products"]
            )

            fig = px.pie(
                category_df,
                names="Category",
                values="Products",
                title="Inventory by Category"
            )

            st.plotly_chart(fig, width="stretch")

    with col2:

        if supplier_data:

            supplier_df = pd.DataFrame(
                supplier_data,
                columns=["Supplier", "Products"]
            )

            fig = px.bar(
                supplier_df,
                x="Supplier",
                y="Products",
                title="Products by Supplier Country"
            )

            st.plotly_chart(fig, width="stretch")

    if destination_data:

        destination_df = pd.DataFrame(
            destination_data,
            columns=["Destination", "Products"]
        )

        fig = px.bar(
            destination_df,
            x="Destination",
            y="Products",
            title="Products by Destination Country",
            text="Products"
        )

    st.plotly_chart(fig, width="stretch")


    st.markdown("---")

    products = ProductService.get_all_products()

    report = AIService.company_advisor(products)

    st.subheader("🤖 Executive AI Brief")

    if report["health"] == "Excellent":
        st.success("🟢 Business Health: Excellent")

    elif report["health"] == "Good":
        st.warning("🟡 Business Health: Good")

    else:
        st.error("🔴 Business Health: Needs Attention")


    if report["critical"]:

        st.markdown("### 🚨 Critical Alerts")

        for item in report["critical"]:
            st.error(item)

    if report["warnings"]:

        st.markdown("### ⚠ Inventory Warnings")

        for item in report["warnings"]:
            st.warning(item)

    if report["recommendations"]:

        st.markdown("### 💡 AI Recommendations")

        for item in report["recommendations"]:
            st.info(item)    

    st.header("Company Overview")

    st.write("""
Welcome to **FOF-AI**.

This intelligent system is designed for **ETS FOFANA CONFISERIE**
to manage inventory, monitor product expiry,
forecast demand, and provide AI-powered business insights.

Current Supplier Countries:

- 🇹🇷 Turkey
- 🇲🇦 Morocco
- 🇹🇳 Tunisia
- 🇧🇷 Brazil

Current Destination Countries:

- 🇲🇱 Mali
- 🇧🇫 Burkina Faso
- 🇨🇮 Côte d'Ivoire
- 🇦🇴 Angola
""")