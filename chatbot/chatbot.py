import streamlit as st
from helpers.constants import SYSTEM_PROMPT, PREDEFINED_PROMPTS
from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Please set it in your environment or .env file.")

openai.api_key = api_key



def display_chatbot():
    """
    Displays a chat interface using Streamlit's chat API.
    Integrates with the OpenAI API to generate responses using gpt-3.5-turbo.
    The system prompt is included for context but hidden from display.
    """

    # Prep session state for messages
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if not any(msg["role"] == "system" for msg in st.session_state["messages"]):
        st.session_state["messages"].append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

    for msg in st.session_state["messages"]:
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


    # User input
    user_text = st.chat_input("Type your question about PyKale here...")

    if user_text:
        st.session_state["messages"].append({"role": "user", "content": user_text})

        with st.chat_message("user"):
            st.write(user_text)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"],
            temperature=0.7,
        )

        bot_text = response.choices[0].message.content.strip()

        st.session_state["messages"].append({
            "role": "assistant",
            "content": bot_text
        })
        
        with st.chat_message("assistant"):
            st.write(bot_text)
