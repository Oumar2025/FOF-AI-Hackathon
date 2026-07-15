import streamlit as st

from services.product_service import ProductService
from services.ai_service import AIService


def show_executive_report():

    st.title("📄 Executive AI Business Report")

    st.write(
        "Generate an executive summary of the company."
    )

    if st.button("Generate Report"):

        report = AIService.generate_executive_report()

        st.markdown(report)