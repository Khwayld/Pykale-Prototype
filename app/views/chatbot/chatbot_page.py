import streamlit as st
from views.components.ui import page_header, info_card
from views.chatbot.display_chatbot import display_chatbot
from utils.constants import SUBHEADING_COLOR

def chatbot_page():
    """Chatbot Page for PyKale Assistant"""
    page_header(
        title="💬 PyKale Assistant",
        subtitle="Ask me anything about <strong>PyKale</strong>! Whether you're just starting or need help with advanced topics, I'm here to guide you."
    )

    st.write("---")

    # Instructions Section
    info_card(
        title="📝 How to Use",
        bullets=[
            "💡 <strong>Ask Questions</strong>: Type anything about PyKale (e.g., 'What is domain adaptation?').",
            "🔍 <strong>Get Context</strong>: The chatbot will retrieve relevant PyKale documentation.",
            "🤖 <strong>Receive AI Guidance</strong>: The assistant will provide step-by-step answers.",
            "📌 <strong>Click Links</strong>: Follow references to explore deeper topics."
        ],
        color=SUBHEADING_COLOR
    )

    # Display Assistant
    display_chatbot()