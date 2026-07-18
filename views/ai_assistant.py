import streamlit as st

from services.ai_service import AIService
from components.header import show_header


def show_ai_assistant():

    show_header(
        "🤖 AI Assistant",
        "Ask Gemma 4 questions about your business."
    )

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