import streamlit as st

from services.ai_service import AIService


def show_ai_assistant():

    st.title("🤖 AI Business Assistant")

    st.write(
        "Ask questions about your business."
    )

    question = st.text_input(
        "Ask me anything..."
    )

    if st.button("Ask AI"):

        if question.strip():

            answer = AIService.business_chat(
                question
            )

            st.success(answer)