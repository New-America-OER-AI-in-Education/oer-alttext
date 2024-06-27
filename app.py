import streamlit as st
from config import settings
from PIL import Image
import io
import os

from src.llm import process_image


# parent_dir = os.path.dirname(os.path.abspath(__file__))
# logo_path = os.path.join(parent_dir, "online.jpg")
# page = st_navbar(["Guide", "History", "About"], logo_path=logo_path)
st.logo("online.svg")
# st.write(page)

# Create session state
session_state = st.session_state

if 'feedback' not in session_state:
    session_state.feedback = ""
if 'alt_text' not in session_state:
    session_state.alt_text = ""

with st.sidebar: 
    st.title("Generation Specifics")
    image = st.file_uploader("Upload an image")
    text_verbosity = st.selectbox("Select Text Verbosity", list(settings['verbosity'].keys()))
    language_selection = st.multiselect("Select Languages", options=settings['languages'], default=["English", "Spanish"])
    grade_selection = st.selectbox("Select Grades", options=settings['grade'], index=1)
    robustness = st.selectbox("Robustness", options=settings['robustness'], index=1)    
    character_length = st.slider("Character Length", min_value=0, max_value=250, value=125)
    subject_area = st.selectbox("Select Subject Area", options=settings['subject'], index=8)

    additional_prompt = st.text_input("Additional Prompt Info")

def get_alt_text():
    st.image(image, use_column_width=True)
    pillow_image = Image.open(image)

    alt_text = process_image(pillow_image, language_selection, settings['verbosity'][text_verbosity], grade_selection, robustness, subject_area, character_length, session_state.feedback, additional_prompt)
    
    session_state.alt_text = alt_text

    # st.write("Alt text generated successfully!")
    # st.write(alt_text)

if image is not None and st.sidebar.button("Get Alt Text", use_container_width=True):
    st.write(f"Generating alt text for image with {settings['verbosity'][text_verbosity]} verbosity...")
    get_alt_text()
else:
    st.write("""<div style="border: 2px solid black; opacity:75%; padding: 10px; border-radius: 10px;">Upload a file to generate alt text!<br>\
                Use the lefthand sidebar to specify your alt text preferences</div>""", unsafe_allow_html=True)
    
    # st.write("Use the lefthand sidebar to specify your alt text preferences.")

if session_state.alt_text:
    st.write("Alt text generated successfully!")
    st.write(session_state.alt_text)
    st.text_input("How did we do?", key="feedback", on_change=get_alt_text)

# st.write(session_state)