import streamlit as st
from config import settings

# Create session state
session_state = st.session_state

# Initialize session state variables
if 'prompt' not in session_state:
    session_state.prompt = ""
if 'feedback' not in session_state:
    session_state.feedback = ""
if 'alt_text_1' not in session_state:
    session_state.alt_text_1 = ""
if 'alt_text_2' not in session_state:
    session_state.alt_text_2 = ""
if 'alt_text_3' not in session_state:
    session_state.alt_text_3 = ""

with st.sidebar: 
    st.title("Generation Specifics")
    image = st.file_uploader("Upload an image")
    text_verbosity = st.selectbox("Select Text Verbosity", list(settings['verbosity'].keys()))
    language_selection = st.multiselect("Select Languages", options=settings['languages'], default=["English", "Spanish"])
    grade_selection = st.selectbox("Select Grades", options=["K-5", "6-8", "9-12", "College", "Professional"], index=1)
    robustness = st.selectbox("Robustness", options=settings['robustness'], index=1)

    additional_prompt = st.text_input("Additional Promp Info")

def get_alt_text():
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Set session state with feedback
    st.text_input("How did we do?", key="feedback")
 

if image is not None and st.sidebar.button("Get Alt Text", use_container_width=True):
    st.write(f"Generating alt text for image with {settings['verbosity'][text_verbosity]} verbosity...")
    get_alt_text()

st.write(session_state)