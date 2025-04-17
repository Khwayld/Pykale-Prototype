import streamlit as st
from utils.constants import PAGE_MAP

def display_frames_in_grid(frames, num_cols=3):
    """
    Display a list of images (frames) in a Streamlit grid layout.

    Args:
        frames: A list of images (PIL or ndarray) to be displayed.
        num_cols: Number of columns per row in the grid.
    """
    rows_needed = (len(frames) + num_cols - 1) // num_cols

    for row_idx in range(rows_needed):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            idx = row_idx * num_cols + col_idx
            if idx < len(frames):
                with cols[col_idx]:
                    st.markdown(
                        f"<h5 style='text-align: center;'>Frame {idx + 1}</h5>",
                        unsafe_allow_html=True
                    )
                    st.image(frames[idx])


def render_placeholder_buttons(full_response):
    """
    Check for any placeholders in the chatbot's final response and 
    render the corresponding navigation buttons dynamically.

    Args:
        full_response: The generated text from the assistant.
    """


    for placeholder, (label, slug) in PAGE_MAP.items():
        if placeholder in full_response:
            st.button(
                f"Go to {label}",
                on_click=lambda p=slug: st.session_state.update({"page": p})
            )
