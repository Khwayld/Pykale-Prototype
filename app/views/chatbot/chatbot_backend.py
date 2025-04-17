import os

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def init_chatbot_backend():
    """
    Loads environment variables and initializes the OpenAI client and Chroma DB.

    Returns:
        client, chroma_db
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error("OPENAI_API_KEY not found. Please set it in your environment or .env file.")
        st.stop()

    client = OpenAI(api_key=api_key)

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    chroma_db = Chroma(
        collection_name="pykale_xml",
        embedding_function=embeddings,
        persist_directory="chroma_db",
    )

    return client, chroma_db




def retrieve_relevant_chunks(chroma_db, query, k=3) -> str:
    """
    Search Chroma DB for the top-k chunks relevant to `query`.
    Return them combined into a single context string.
    """
    results = chroma_db.similarity_search(query, k=k)
    context_blocks = []

    for doc in results:
        content = doc.page_content
        context_blocks.append(f"{content}")

    return "\n".join(context_blocks)

