
#from PIL import report
import streamlit as st
import pandas as pd
import plotly.express as px

from services.product_service import ProductService
from services.ai_service import AIService

def flag_row(flag_path, country):
    col1, col2 = st.columns([1, 6])

    with col1:
        st.image(flag_path, width=30)

    with col2:
        st.markdown(f"**{country}**")


def show_dashboard():

    from components.header import show_header

    show_header(
        "🤖 FOF-AI",
        "AI Business Intelligence Assistant"
    )

    stats = ProductService.get_dashboard_statistics()

    st.subheader("📊 Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📦 Products", stats["total_products"])
    col2.metric("⚠ Low Stock", stats["low_stock"])
    col3.metric("📅 Expiring Soon", stats["expiring_soon"])
    col4.metric("🌍 Countries", stats["countries"])

    st.markdown("---")

    st.subheader("🚨 Smart Business Alerts")

    st.info("""
    ### 🎯 Priority Actions Today

    Review today's alerts before making import or promotion decisions.

    The AI recommendations below are generated from your current inventory, expiry dates, and business trends.
    """)

    products = ProductService.get_all_products()

    report = AIService.company_advisor(products)

    st.subheader("🧠 AI Business Advisor")

    if report["health"] == "Excellent":
        st.success("🟢 Overall Business Health: Excellent")

    elif report["health"] == "Good":
        st.warning("🟡 Overall Business Health: Good")

    else:
        st.error("🔴 Overall Business Health: Needs Attention")


    if report["critical"]:

        st.markdown("### 🔴 Immediate Attention")

        for item in report["critical"]:
            st.error(item)

    if report["warnings"]:

        st.markdown("### 🟡 Inventory Warnings")

        for item in report["warnings"]:
            st.warning(item)

    if report["recommendations"]:

        st.markdown("### 💡 Recommended Actions")

        for item in report["recommendations"]:
            st.info(item) 

    if st.button("📧 Check & Send Alerts"):

        AIService.check_and_send_alerts()

        st.success("✅ Alert check completed successfully!")

    

    st.markdown("---")

    st.subheader("📈 Business Analytics")

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
            fig.update_layout(
                template="plotly_dark",
                margin=dict(l=20, r=20, t=50, b=20),
                height=380,
            )

            st.plotly_chart(fig, use_container_width=True)
            st.write("")        

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
            fig.update_layout(
                template="plotly_dark",
                margin=dict(l=20, r=20, t=50, b=20),
                height=380,
            )

            st.plotly_chart(fig, use_container_width=True)
            st.write("")
    
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
        fig.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=50, b=20),
            height=380,
        )

        st.plotly_chart(fig, use_container_width=True)

        st.write("")
    
    st.markdown("---")

       

    st.header("🏢 Company Overview")

    st.write("""
    Welcome to **FOF-AI**.

    This intelligent system is designed for **ETS FOFANA CONFISERIE**
    to manage inventory, monitor product expiry,
    forecast demand, and provide AI-powered business insights.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🌍 Supplier Countries")

        flag_row("assets/flags/turkey.png", "Turkey")
        flag_row("assets/flags/morocco.png", "Morocco")
        flag_row("assets/flags/tunisia.png", "Tunisia")
        flag_row("assets/flags/brazil.png", "Brazil")


    with col2:

        st.subheader("✈️ Destination Countries")

        flag_row("assets/flags/mali.png", "Mali")
        flag_row("assets/flags/burkina_faso.png", "Burkina Faso")
        flag_row("assets/flags/cote_divoire.png", "Côte d'Ivoire")
        flag_row("assets/flags/angola.png", "Angola")