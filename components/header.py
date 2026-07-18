import streamlit as st


def show_header(title: str, subtitle: str):
    st.title(title)
    st.caption(subtitle)
    st.markdown("")