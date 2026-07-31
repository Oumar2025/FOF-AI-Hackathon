import streamlit as st


def show_logo_header(subtitle, show_login_text=False):

    # -------- Company Logo --------
    left, center, right = st.columns([2, 1, 2])

    with center:
        st.image(
            "assets/logo.png",
            width=260        # Bigger company logo
        )

    # Reduce vertical spacing
    st.markdown(
        "<div style='margin-top:-15px;'></div>",
        unsafe_allow_html=True
    )

    # -------- AI Logo + Title --------
    left, center, right = st.columns([2, 1.6, 2])

    with center:

        icon_col, text_col = st.columns([0.7, 3.3])

        with icon_col:
            st.image(
                "assets/lo.png",
                width=42      # Smaller AI icon
            )

        with text_col:
            st.markdown(
                """
                <h1 style="
                    font-size:48px;
                    font-weight:700;
                    margin-top:5px;
                    margin-bottom:0;
                ">
                FOF-AI
                </h1>
                """,
                unsafe_allow_html=True,
            )

    # Almost no space before subtitle
    st.markdown(
        f"""
        <h3 style="
            text-align:center;
            color:gray;
            margin-top:-10px;
        ">
        {subtitle}
        </h3>
        """,
        unsafe_allow_html=True,
    )

    if show_login_text:

        st.markdown(
            """
            <p style="
                text-align:center;
                margin-top:-5px;
            ">
            Please sign in to continue
            </p>
            """,
            unsafe_allow_html=True,
        )