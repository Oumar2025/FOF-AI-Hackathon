import streamlit as st


def show_sidebar():

    st.sidebar.markdown(
        """
        <h1 style='text-align:center; margin-bottom:0;'>
        🤖 FOF-AI
        </h1>

        <p style='text-align:center;
        color:#94A3B8;
        margin-top:0;'>
        AI Business Intelligence
        </p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    menu = st.sidebar.pills(
        "Navigation",
        [
            "📊 Dashboard",
            "📦 Inventory",
            "📈 Forecast",
            "🤖 AI Assistant",
            "📋 Executive Report",
            "⚙️ Settings"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.success("🟢 AI System Online")

    st.sidebar.info(
        """
### 🏢 ETS FOFANA CONFISERIE

AI Business Intelligence Assistant

Built with Gemma 4
"""
    )

    return menu