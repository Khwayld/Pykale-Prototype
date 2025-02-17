import streamlit as st


def display_frames_in_grid(frames, num_cols=3):
    """
    Helper function to display a list of frames (PIL images or arrays) in a grid layout.
    Each row has `num_cols` columns.
    """
    rows_needed = (len(frames) + num_cols - 1) // num_cols
    for row_idx in range(rows_needed):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            frame_index = row_idx * num_cols + col_idx
            if frame_index < len(frames):
                with cols[col_idx]:
                    st.markdown(
                        f"<h5 style='text-align: center;'>Frame {frame_index + 1}</h5>",
                        unsafe_allow_html=True
                    )
                    st.image(frames[frame_index], use_column_width=True)


def load_file(file_path: str) -> str:
    """Load a file from the given path and return as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    

