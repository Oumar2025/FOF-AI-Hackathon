import streamlit as st

from services.product_service import ProductService
from services.ai_service import AIService
from components.header import show_header


def show_executive_report():

    show_header(
        "📋 Executive Report",
        "AI-generated business intelligence summary."
    )

    st.write(
        "Generate an executive summary of the company."
    )

    if st.button("Generate Report"):

        report = AIService.generate_executive_report()

        st.markdown(report)