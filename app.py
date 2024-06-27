import streamlit as st
from config import settings
from PIL import Image
import io

from src.llm import process_image


with st.sidebar: 
    st.title("Generation Specifics")
    image = st.file_uploader("Upload an image")
    text_verbosity = st.selectbox("Select Text Verbosity", list(settings['verbosity'].keys()))
    language_selection = st.multiselect("Select Languages", options=settings['languages'], default=["English", "Spanish"])
    grade_selection = st.selectbox("Select Grades", options=settings['grade'], index=1)
    robustness = st.selectbox("Robustness", options=settings['robustness'], index=1)    
    character_length = st.slider("Character Length", min_value=0, max_value=250, value=125)
    subject_area = st.selectbox("Select Subject Area", options=settings['subject'], index=8)


def get_alt_text():
    pillow_image = Image.open(image)

    alt_text = process_image(pillow_image, language_selection, settings['verbosity'][text_verbosity], grade_selection, robustness, subject_area, character_length)
    
    st.write("Alt text generated successfully!")
    st.write(alt_text)

    st.button("Regenerate Alt Text", on_click=get_alt_text)


if image is not None and st.sidebar.button("Get Alt Text", use_container_width=True):
    st.write(f"Generating alt text for image with {settings['verbosity'][text_verbosity]} verbosity...")
    get_alt_text()
