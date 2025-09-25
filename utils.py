from PIL import Image
import streamlit as st


def handle_file_upload():
    """Handle image upload from sidebar."""
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.session_state.image = image
        st.image(image, caption="Uploaded Image", use_container_width=True)
    return st.session_state.get("image", None)
