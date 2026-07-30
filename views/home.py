import streamlit as st


def show_home():

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.image(
            "assets/logo.png",
            width=220
        )

        st.markdown(
            """
            <h1 style='text-align:center;'>
            🤖 FOF-AI
            </h1>

            <h4 style='text-align:center;color:gray;'>
            AI Business Intelligence Platform
            </h4>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("🏢 Welcome")

    st.write(
        """
Welcome to **FOF-AI**, an Artificial Intelligence Business Intelligence System
developed for **ETS FOFANA CONFISERIE**.

The platform assists managers in monitoring inventory, forecasting demand,
tracking product expiry, and supporting better business decisions through AI.
"""
    )

    st.markdown("---")

    st.subheader("🌍 Business Coverage")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
### Supplier Countries

- 🇹🇷 Turkey
- 🇲🇦 Morocco
- 🇹🇳 Tunisia
- 🇧🇷 Brazil
"""
        )

    with col2:

        st.markdown(
            """
### Destination Countries

- 🇲🇱 Mali
- 🇧🇫 Burkina Faso
- 🇨🇮 Côte d'Ivoire
- 🇦🇴 Angola
"""
        )

    st.markdown("---")

    st.subheader("✨ Main Modules")

    st.markdown(
        """
- 📊 Dashboard
- 📦 Inventory Management
- 📈 Demand Forecast
- 🤖 AI Business Advisor
- 🚨 Smart Alerts
- 📋 Executive Reports
"""
    )

    st.markdown("---")

    st.success(
        "Select a module from the left sidebar to begin using FOF-AI."
    )