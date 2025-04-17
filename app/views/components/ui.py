import streamlit as st
from navigation.navigation import go_to
from utils.constants import PRIMARY_COLOR

def page_header(title, subtitle=""):
    """
    Renders a page header with a title and an optional subtitle

    Args:
        title: Main page title
        subtitle: Optional subheading below the title
    """
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color:{PRIMARY_COLOR};">{title}</h1>
            {"<p style='font-size:16px; max-width:700px; margin:auto; padding-bottom: 20px;'>" + subtitle + "</p>" if subtitle else ""}
        </div>
        """, 
        unsafe_allow_html=True
    )



def button_component(button_text, slug, centering=[3, 1.5, 3]):
    """
    Renders a centered navigation button component

    Args:
        button_text: The title of the button
        slug: The navigation destination of the button
        centering: Optional, adjust centering of button
    """
    col_left, col_center, col_right = st.columns(centering)
    with col_center:
        if st.button(button_text):
            go_to(slug)

    st.markdown("---")



def info_card(title, bullets, subtitle="", footer_note=None, color=PRIMARY_COLOR):
    """
    Renders a centered summary block with bullet points and optional footer.

    Args:
        title: The title of the summary section.
        bullets: A list of bullet point strings.
        subtitle: An optional paragraph before the bullets.
        footer_note: An optional paragraph after the bullets.
        color: Color of title
    """
    bullet_html = "".join([f"<li>{b}</li>" for b in bullets])

    st.markdown(
        f"""
        <div style="text-align: center; max-width: 700px; margin:auto;">
            <h3 style="color:{color};">{title}</h3>
            {"<p style='font-size:16px; max-width:700px; margin:auto; padding-bottom: 20px;'>" + subtitle + "</p>" if subtitle else ""}
            <ul style="display:inline-block; text-align:left; padding: 0; margin: 0;">
                {bullet_html}
            </ul>
            {'<p style="margin-top: 10px;">' + footer_note + '</p>' if footer_note else ''}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")



def section_block(title, body= "", heading_level=4, color="#16a085"):
    """
    Renders a reusable section with a heading and an optional paragraph.

    Args:
        title: The section title.
        body: Optional paragraph text (supports HTML).
        heading_level: HTML heading level to use (e.g., 2, 3, 4). Default is 4.
        color: Text color for the heading.
    """
    st.markdown(f"<h{heading_level} style='text-align:center; color:{color};'>{title}</h{heading_level}>", unsafe_allow_html=True)
    
    if body.strip():
        cleaned_body = body.strip().replace("\n", " ")
        st.markdown(f"<p style='text-align:center;'>{cleaned_body}</p>", unsafe_allow_html=True)


def code_snippet_block(label, code, write_up=""):
    """
    Reusable code section with expand/collapse.
    
    Args:
        label: The label of the expander.
        code: The code snippet.
        write_up: An optional paragraph to explain the code snippet.
    """
    with st.expander(label):
        if write_up !="":
            st.write(write_up)
        
        st.code(code, language="python")