## 🧐 About
This project was developed as part of a university dissertation and aims to improve the accessibility of the [PyKale](https://github.com/pykale/) library, a powerful framework for multimodal and transfer learning, for interdisciplinary research. 

To achieve this, the prototype integrates:

- A Retrieval-Augmented Generation (RAG) chatbot trained on PyKale codebase.

- An interactive Streamlit-based web interface with embedded explanations and usage flows.

- A simple no-code model training demo to showcase PyKale's capabilities without requiring any programming experience.

While functional, this prototype was developed under strict time constraints. The code may lack optimal structure, some modules are tightly coupled, and refactoring is planned for post-submission cleanup.


## 🏁 Getting Started
To run the project locally, clone the repo and install the required dependencies.

### Prerequisites
- Python 3.10+
- OpenAI API Key

Install required packages:
```
pip install -r requirements.txt
```

Set your API key in a .env file:
```
OPENAI_API_KEY=your_key_here
```

Start the app:
```
streamlit run main.py
```

## 🚀 Deployment
The app is currently [deployed](https://pykale.streamlit.app/) using Streamlit Cloud, which comes with limitations (no GPU support). Future plans include migrating to a custom server with GPU access for heavier model training tasks.


## ⛏️ Built Using
- Streamlit - Web UI
- LangChain - Chatbot backend
- ChromaDB - Vector store for RAG
- OpenAI API - LLM and embeddings 
- PyKale - ML backend

## ✅ To Do
- Refactor backend logic into cleaner modules
- Add more trainers to the no-code section 
- Expand chatbot knowledge base 
- Deploy with GPU-backed infrastructure