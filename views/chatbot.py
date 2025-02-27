import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from helpers.helper import load_file
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Please set it in your environment or .env file.")

client = OpenAI(
    api_key=api_key,  
)

SYSTEM_PROMPT = load_file("./datasets/pykale_prompt.txt")

embeddings = OpenAIEmbeddings(openai_api_key=api_key)
chroma_db = Chroma(
    collection_name="pykale_xml",
    embedding_function=embeddings,
    persist_directory="chroma_db",
)

def retrieve_relevant_chunks(query: str, k=3) -> str:
    """
    Search Chroma DB for the top-k chunks relevant to `query`.
    Return them combined into a single context string.
    """
    docs = chroma_db.similarity_search(query, k=k)
    # Each doc has `doc.page_content` and `doc.metadata`
    context_blocks = []
    for d in docs:
        src = d.metadata.get("source", "unknown")
        content = d.page_content
        context_blocks.append(f"[Source: {src}]\n{content}")
    return "\n\n".join(context_blocks)



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

        context = retrieve_relevant_chunks(user_text, k=3)

        temp_messages = st.session_state["messages"][:]
        temp_messages.append({
            "role": "system",
            "content": f"Relevant context:\n{context}"
        })

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=temp_messages
        )

        bot_text = response.choices[0].message.content.strip()

        st.session_state["messages"].append({
            "role": "assistant",
            "content": bot_text
        })
        
        with st.chat_message("assistant"):
            st.write(bot_text)
