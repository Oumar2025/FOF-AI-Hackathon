import streamlit as st
from components.logo_header import show_logo_header


def show_header(title, subtitle):

    show_logo_header(
        subtitle=subtitle,
        show_login_text=False
    )

    st.markdown("")