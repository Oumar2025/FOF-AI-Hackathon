import streamlit as st


def show_logo_header(subtitle, show_login_text=False):

    # Center the company logo
    left, center, right = st.columns([2, 1, 2])

    with center:
        st.image("assets/logo.png", width=200)

    st.write("")

    # Center the AI logo + title
    left, center, right = st.columns([2, 2, 2])

    with center:
        icon_col, text_col = st.columns([1, 4])

        with icon_col:
            st.image("assets/lo.png", width=55)

        with text_col:
            st.markdown(
                """
                <h1 style="margin-top:10px;">
                FOF-AI
                </h1>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        f"""
        <h3 style="text-align:center;color:gray;">
        {subtitle}
        </h3>
        """,
        unsafe_allow_html=True,
    )

    if show_login_text:
        st.markdown(
            """
            <p style="text-align:center;">
            Please sign in to continue
            </p>
            """,
            unsafe_allow_html=True,
        )