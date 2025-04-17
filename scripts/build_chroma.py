import os
import openai
import chromadb

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


def build_index(xml_path, persist_dir="chroma_db"):
    """
    Builds a Chroma vector database from a given XML document using OpenAI embeddings. 

    Args:
        xml_path: Path to XML file.
        persist_dir: Directory where the Chroma DB will be saved. 
    """

    # Load env variables
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")

    # Read file content
    with open(xml_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    # Init Chroma client
    chroma_client = chromadb.PersistentClient(path=persist_dir)

    # Use OpenAI embeddings to convert chunks into vectors
    embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
    
    # Build vector store
    Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=[{"source": "pykale.xml"} for _ in chunks],
        collection_name="pykale_xml",
        client=chroma_client,
    )

    print(f"Chroma DB built in: {persist_dir}")


if __name__ == "__main__":
    xml_path = "./data/pykale.xml" 
    build_index(xml_path)
