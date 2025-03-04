import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini Model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Chatbot")
st.write("Ask me anything!")

# User Input
user_input = st.text_input("You:", "")

if user_input:
    response = model.generate_content(user_input)
    st.write("🤖 AI:", response.text)
