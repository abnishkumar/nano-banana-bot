import streamlit as st


avatars = {
    "assistant": "🤖",
    "user": "👤"
}


def init_chat():
    """Initialize chat history if not exists."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "How may I assist you today?", "image": None}
        ]


def display_messages():
    """Display chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=avatars[message["role"]]):
            st.write(message["content"])
            if message["role"] == "assistant" and message["image"]:
                st.image(message["image"])


def add_message(role, content, image=None):
    """Add a new message to chat history."""
    st.session_state.messages.append(
        {"role": role, "content": content, "image": image}
    )


def clear_history():
    """Clear chat history."""
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?", "image": None}
    ]
