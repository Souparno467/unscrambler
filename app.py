import streamlit as st
import google.generativeai as gemini
from dotenv import load_dotenv,find_dotenv
import os

# Configure the Gemini API with a hardcoded API key
load_dotenv(find_dotenv(),override=True)
api_key = os.getenv("GOOGLE_API_KEY")
gemini.configure(api_key=api_key)
model = gemini.GenerativeModel("gemini-1.5-pro")


# Function to unscramble the word using Google Generative AI
def unscramble_with_ai(scrambled_word):
    prompt = (
                f"Unscramble the following word: {scrambled_word} and Include its part of speech, a brief definition and an example sentence"
               )
    response = model.generate_content(prompt)

    if response and response.text:
        return response.text.strip()  # Return the generated text
    else:
        return "Error: Unable to unscramble the word."

# Streamlit app layout
st.set_page_config(
    page_title="🧩AI Word Unscrambler🧩",
    page_icon="🧩",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f0f2f5;
        font-family: 'Helvetica', sans-serif;
    }
    .title {
        font-size: 40px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
    }
    .input {
        margin: 20px 0;
        text-align: center;
    }
    .result {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-top: 20px;
    }
    .warning {
        color: #FF5733;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧩AI Word Unscrambler🧩</div>', unsafe_allow_html=True)

# Input for scrambled word
scrambled_word = st.text_input("Enter a scrambled word:", placeholder="e.g., soine")

# Unscramble button
if st.button("Unscramble"):
    if scrambled_word:
        result = unscramble_with_ai(scrambled_word.lower())
        st.markdown(f'<div><u>{result}</u></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="warning">Please enter a scrambled word.</div>', unsafe_allow_html=True)
