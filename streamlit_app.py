import streamlit as st
import requests

# API Key
API_KEY = "AIzaSyAagGHcfP1qm9TdimloHN40fJMCjqKceH0"  # Replace with your actual API key

# Page configuration
st.set_page_config(page_title="Gurug", page_icon="🧠", layout="centered")

# CSS Styling for responsiveness and aesthetics
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .stTextInput>div>div>input {
            text-align: center;
            font-size: 16px;
        }
        .stButton button {
            width: 100%;
            font-size: 18px;
            background-color: #4285F4;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .response-box {
            background-color: #f9f9f9;
            border-left: 5px solid #4285F4;
            padding: 15px;
            border-radius: 6px;
            font-size: 16px;
        }
        @media only screen and (max-width: 600px) {
            .stTextInput>div>div>input {
                font-size: 14px;
            }
            .stButton button {
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Logo/title
st.markdown("<h1 class='centered' style='color:#4285F4;'>Gurug</h1>", unsafe_allow_html=True)


# Input with placeholder
placeholder_text = "शीर्षक दियर गित, कथा, कविता, लेख्न लगाऊनुहोस वा खोज्नुहोस.."
query = st.text_input("", placeholder=placeholder_text)

# Button to trigger
search = st.button("🔍 Search")

# Process on click
if search:
    if not query.strip() or query == placeholder_text:
        st.warning("Please type something.")
    else:
        st.info("Thinking...")

        # Gemini API call
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": API_KEY
        }
        payload = {
            "contents": [
                {
                    "parts": [{"text": query}]
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            data = response.json()
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            st.markdown(f"<div class='response-box'>{reply}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("Something went wrong. Please check your API key or internet connection.")
            st.code(str(e))
