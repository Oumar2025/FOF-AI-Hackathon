import streamlit as st
from components.logo_header import show_logo_header


def flag_row(flag_path, country):
    col1, col2 = st.columns([1, 6])

    with col1:
        st.image(flag_path, width=32)

    with col2:
        st.markdown(f"**{country}**")

def show_home():

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        show_logo_header(
            subtitle="AI Business Intelligence Platform"
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