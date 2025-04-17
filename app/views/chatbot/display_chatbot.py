import streamlit as st
from utils.ui_utils import render_placeholder_buttons
from utils.helper_utils import load_file, remove_placeholders
from views.chatbot.chatbot_backend import init_chatbot_backend, retrieve_relevant_chunks


# Setup OpenAI + Chroma backend
client, chroma_db = init_chatbot_backend()
SYSTEM_PROMPT = load_file("./data/pykale_prompt.txt")


def display_chatbot():
    """
    Displays a chat interface using Streamlit's chat API.
    Integrates with the OpenAI API to generate responses.
    """

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Inject system prompt 
    if not any(msg["role"] == "system" for msg in st.session_state["messages"]):
        st.session_state["messages"].append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

    # Display chat history
    for msg in st.session_state["messages"]:
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


    user_text = st.chat_input("Type your question about PyKale here...")

    if user_text:
        st.session_state["messages"].append({"role": "user", "content": user_text})

        with st.chat_message("user"):
            st.write(user_text)

        # Retrieve relevant context
        context = retrieve_relevant_chunks(chroma_db, user_text, k=3)

        # Inject
        st.session_state["messages"].append({
            "role": "system",
            "content": f"Relevant context:\n{context}"
        })

        # Stream response from OpenAI
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


        # Save response to session state
        st.session_state["messages"].append({
            "role": "assistant",
            "content": full_response
        })
        

        # Post-process the final response. 
        final_text = remove_placeholders(full_response)
        text_placeholder.markdown(final_text)
        render_placeholder_buttons(full_response)
