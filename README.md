# PyKale Streamlit Prototype
A **Streamlit-powered web interface** demonstrating different use cases for [PyKale](https://github.com/pykale/pykale) with a **AI powered chatbot** that references a local Chroma DB for context awareness.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
---

## Overview
**What is this project?**  
This repository provides a **user-friendly Streamlit interface** that allows users to interact with PyKale functionalities without requiring in-depth coding knowledge. 

**Key Goals:**
1. **Bridge the technical gap** for non-expert users by providing an accessible UI.
2. **Demonstrate key functionalities** that PyKale provides.
3. **Enhance usability** with an AI-powered chatbot that provides context-aware answers. 

---
## Features
- todo
---

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/YourUsername/pykale-streamlit-demo.git
cd pykale-streamlit-demo
```

2. **Install Python Requirements**
- Create or activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


- Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Configure Environment Variables**
- If you plan to use the OpenAI chatbot, set `OPENAI_API_KEY` as an environment variable or add it to a `.env` file (the repository uses `dotenv` to load it).

4. **(Optional) Build or Update Chroma DB**
- If you have new data or want to refresh existing data for the chatbot’s retrieval, run:
```bash
python build_chroma.py
```
- This will create/update the local Chroma database that the chatbot queries for contextual information.


## Usage
1. **Run the Streamlit App**
```bash
streamlit run main.py
```
