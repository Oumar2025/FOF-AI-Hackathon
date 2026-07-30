import streamlit as st


USERNAME = "Fofana"
PASSWORD = "2004Fofana"


def show_login():

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.image(
            "assets/logo.png",
            width=220
        )

        st.markdown(
            """
            <h1 style='text-align:center;'>
            🤖 FOF-AI
            </h1>

            <h3 style='text-align:center;color:gray;'>
            AI Business Intelligence Platform
            </h3>

            <p style='text-align:center;'>
            Please sign in to continue
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

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