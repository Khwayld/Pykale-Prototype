# chatbot.py
import streamlit as st
import numpy as np

def display_chatbot():
    """
    Displays a chat interface using Streamlit's new chat API (st.chat_message, st.chat_input).
    Keeps conversation in session_state.
    """

    if "messages" not in st.session_state:
        st.session_state["messages"] = []


    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


    user_text = st.chat_input("Type your message here...")


    if user_text:
        st.session_state["messages"].append({
            "role": "user",
            "content": user_text
        })
        with st.chat_message("user"):
            st.write(user_text)


        bot_text = f"Hello! You said: {user_text}"


        st.session_state["messages"].append({
            "role": "assistant",
            "content": bot_text,
        })


        with st.chat_message("assistant"):
            st.write(bot_text)
