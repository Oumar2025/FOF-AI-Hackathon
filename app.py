import streamlit as st
import pandas as pd
import plotly.express as px
from models.product import Product
from services.product_service import ProductService
from pages.dashboard import show_dashboard
from pages.inventory import show_inventory
from pages.forecast import show_forecast
from pages.ai_assistant import show_ai_assistant
from pages.executive_report import show_executive_report

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="FOF-AI",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.title("🤖 FOF-AI")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Inventory",
        "Forecast",
        "AI Assistant",
        "Executive Report",
        "Settings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "ETS FOFANA CONFISERIE\n\n"
    "AI Business Intelligence Assistant"
)

# -------------------------------------------------
# Dashboard
# -------------------------------------------------

if menu == "Dashboard":
    show_dashboard()
    
# -------------------------------------------------
# Inventory Page
# -------------------------------------------------

elif menu == "Inventory":
    show_inventory()      

elif menu == "Forecast":
    show_forecast()

elif menu == "AI Assistant":
    show_ai_assistant()

elif menu == "Executive Report":
    show_executive_report()    