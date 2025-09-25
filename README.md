🍌 Gemini Nano Banana Chatbot

An AI-powered image generator chatbot built with Streamlit and Google Gemini API.
This chatbot allows you to chat with an assistant 🤖, generate images from text prompts, and even modify uploaded images.


⚙️ Installation

- Clone the repository

git clone https://github.com/abnishkumar/nano-banana-bot.git
cd nano-banana-bot


Create a virtual environment (i am using uv package manager you can use pip that is up to you.)

uv venv
.venv\Scripts\activate
Install dependencies
uv add -r requirements.txt

Add your Gemini API key
Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

# Running the App
streamlit run app.py