import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Bhaiya & Company Chatbot", page_icon=":robot:", layout="wide")

# Sidebar for logo with custom background color
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #2C3E50;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

with st.sidebar:
    logo = Image.open("C:/Users/bhaiyasingh/Downloads/logo.webp")
    st.image(logo, use_column_width=True)
    st.markdown("<h3 style='text-align: center; color: #ECF0F1;'>Bhaiya & Company</h3>", unsafe_allow_html=True)

# Header with background color and centered text
st.markdown(
    """
    <div style="background-color: #2a59b8; padding: 5px;">
        <h3 style='text-align: center; color: white;'>
        Bhaiya & Company Chatbot
        </h3>
    </div>
    """, unsafe_allow_html=True
)

# Main chat area styling
st.markdown(
    """
    <style>
    .chat-box {
        background-color: #ECF0F1;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<div class='chat-box'><p style='color: #2C3E50;'>Welcome to the Bhaiya & Company Chatbot. How can I assist you today?</p></div>", unsafe_allow_html=True)

# Input field for user queries
user_input = st.text_input("You:", "")

# Display chatbot response with styling
if user_input:
    response = "This is where the chatbot's response will appear."
    st.markdown(f"<div class='chat-box'><p style='color: #2C3E50;'>Bhaiya & Company Chatbot: {response}</p></div>", unsafe_allow_html=True)

# Fixed footer with copyright notice
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #2C3E50;
        color: white;
        text-align: center;
        padding: 3px;
    }
    </style>
    <div class="footer">
        © Bhaiya & Company 2024
    </div>
    """, unsafe_allow_html=True
)