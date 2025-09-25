import streamlit as st
from chatbot import init_chat, display_messages, add_message, clear_history
from utils import handle_file_upload
from gemini_client import GeminiClient


st.set_page_config(page_title="Gemini Nano Banana Chatbot",
                   initial_sidebar_state="auto")

# Title
st.markdown("<h2 style='text-align: center; color: #3184a0;'>Gemini Nano Banana</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #3184a0;'>Image generator chatbot</h3>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🍌 Gemini Nano Banana")
    st.button("Clear Chat History", on_click=clear_history)
    uploaded_image = handle_file_upload()

# Init chat
init_chat()
display_messages()

# Input box
if prompt := st.chat_input("Type your request..."):
    add_message("user", prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Generating response..."):
            gemini = GeminiClient()
            print(prompt , uploaded_image)
            response = gemini.generate(prompt, uploaded_image)

            text_output, image_output = None, None
            if response and response.candidates:
                for part in response.candidates[0].content.parts:
                    if part.text:
                        text_output = part.text
                    if part.inline_data and part.inline_data.data:
                        image_output = part.inline_data.data

            # Display text
            if text_output:
                st.write(text_output)

            # Display image
            if image_output:
                st.image(image_output)

            add_message("assistant", text_output or "No text generated", image_output)
