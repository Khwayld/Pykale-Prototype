# build_chroma.py
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import openai

def build_index(xml_path, persist_dir="chroma_db"):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in environment or .env")

    # 1) Read your pykale.xml
    with open(xml_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 2) Chunk the text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = text_splitter.split_text(text)

    # 3) Create embeddings & store in Chroma
    embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=[{"source": "pykale.xml"} for _ in chunks],
        collection_name="pykale_xml",
        persist_directory=persist_dir
    )

    # 4) Persist
    vectordb.persist()
    print(f"Chroma DB built & persisted in: {persist_dir}")

if __name__ == "__main__":
    xml_path = "./datasets/pykale.xml"  # or wherever your pykale.xml is
    build_index(xml_path)
