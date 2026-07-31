import streamlit as st

from components.logo_header import show_logo_header


USERNAME = "Fofana"
PASSWORD = "2004Fofana"


def show_login():

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        show_logo_header(
            subtitle="AI Business Intelligence Platform",
            show_login_text=True
        )
        username = st.text_input(
            "Username",
            placeholder="ENTER USERNAME"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="ENTER PASSWORD"
        )

        remember = st.checkbox("Remember me")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Login",
            use_container_width=True
        ):

            if (
                username == USERNAME
                and
                password == PASSWORD
            ):

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

        st.markdown("<br><br>")

        st.caption(
            "© 2026 ETS FOFANA CONFISERIE. All rights reserved."
        )