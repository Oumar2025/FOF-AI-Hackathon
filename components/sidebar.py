import streamlit as st


def show_sidebar():

    st.sidebar.image(
        "assets/lo.png",
        use_container_width=True
    )

    st.sidebar.markdown(
        """
        <p style='text-align:center;
        color:#94A3B8;
        margin-top:5px;'>
        AI Business Intelligence
        </p>
        """,
        unsafe_allow_html=True
    )

    # Initialize current page
    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Home"

    st.sidebar.markdown("### Navigation")

    pages = [
        "🏠 Home",
        "📊 Dashboard",
        "📦 Inventory",
        "📈 Forecast",
        "🤖 AI Assistant",
        "📋 Executive Report",
        "🚨 Alert Center",
        "⚙️ Settings",
    ]

    for page in pages:

        if page == st.session_state.menu:
            button_type = "primary"
        else:
            button_type = "secondary"

        if st.sidebar.button(
            page,
            use_container_width=True,
            type=button_type,
            key=page,
        ):
            st.session_state.menu = page
            st.rerun()

    menu = st.session_state.menu


    st.sidebar.markdown("---")

    st.sidebar.success("🟢 AI System Online")

    st.sidebar.info(
        """
### 🏢 ETS FOFANA CONFISERIE

AI Business Intelligence Assistant

Built with Gemma 4
"""
    )

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.rerun()

    return menu

