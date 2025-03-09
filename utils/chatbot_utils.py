import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from helpers.helper import load_file, remove_placeholders, render_placeholder_buttons_if_needed
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


# Initialize Open AI Client
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Please set it in your environment or .env file.")

client = OpenAI(
    api_key=api_key,  
)

SYSTEM_PROMPT = load_file("./datasets/pykale_prompt.txt")


# Initialize Chroma DB
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

        st.session_state["messages"].append({
            "role": "system",
            "content": f"Relevant context:\n{context}"
        })

        with st.chat_message("assistant"):
            text_placeholder = st.empty()
            full_response = ""

            response_stream = client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state["messages"],
                stream=True
            )

            for chunk in response_stream:
                if chunk.choices:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, "content") and delta.content:
                        full_response += delta.content
                        text_placeholder.markdown(full_response)


        st.session_state["messages"].append({
            "role": "assistant",
            "content": full_response
        })
        

        final_text = remove_placeholders(full_response)
        text_placeholder.markdown(final_text)
        render_placeholder_buttons_if_needed(full_response)
