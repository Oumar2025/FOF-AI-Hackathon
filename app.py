import streamlit as st
import pandas as pd
import plotly.express as px
from models.product import Product
from services.product_service import ProductService
from views.dashboard import show_dashboard
from views.inventory import show_inventory
from views.forecast import show_forecast
from views.ai_assistant import show_ai_assistant
from views.executive_report import show_executive_report
# -------------------------------------------------
# Page Configuration
# -------------------------------------------------


st.set_page_config(
    page_title="FOF-AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

[data-testid="stSidebarNav"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Logo */

.sidebar-title{
    font-size:34px;
    font-weight:bold;
    text-align:center;
    padding-bottom:20px;
}

/* Radio buttons */

div[role="radiogroup"] label{

    font-size:20px !important;

    padding:12px 8px;

    border-radius:10px;

    margin-bottom:8px;

}

/* Navigation title */

.sidebar-subtitle{

    font-size:22px;

    font-weight:bold;

    margin-top:15px;

    margin-bottom:10px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

from components.sidebar import show_sidebar

menu = show_sidebar()

# -------------------------------------------------
# Dashboard
# -------------------------------------------------

if menu == "📊 Dashboard":
    show_dashboard()
    
# -------------------------------------------------
# Inventory Page
# -------------------------------------------------

elif menu == "📦 Inventory":
    show_inventory()      

elif menu == "📈 Forecast":
    show_forecast()

elif menu == "🤖 AI Assistant":
    show_ai_assistant()

elif menu == "📋 Executive Report":
    show_executive_report()    