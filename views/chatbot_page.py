import streamlit as st
from utils.chatbot_utils import display_chatbot

def chatbot_page():
    """Chatbot Page for PyKale Assistance with Clear Title and Instructions."""
    
    # Header Section
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>💬 PyKale Assistant – Your AI Guide to PyKale</h1>
            <p style="font-size:18px;">
                Ask me anything about <strong>PyKale</strong>! Whether you're just starting 
                or need help with advanced topics, I'm here to guide you.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # Instructions Section
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>📝 How to Use</h3>
            <ul style="display: inline-block; text-align: left;">
                <li>💡 <strong>Ask Questions</strong>: Type anything about PyKale (e.g., "What is domain adaptation?").</li>
                <li>🔍 <strong>Get Context</strong>: The chatbot will retrieve relevant PyKale documentation.</li>
                <li>🤖 <strong>Receive AI Guidance</strong>: The assistant will provide step-by-step answers.</li>
                <li>📌 <strong>Click Links</strong>: Follow references to explore deeper topics.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    display_chatbot()