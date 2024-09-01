import streamlit as st
from PIL import Image
from utilities.utils import stream_data, get_prompts_dict

# <--------------------------------------- Streamlit Page ---------------------------------------------------->

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
    logo = Image.open("C:\My Repos\RAG-Chatbot\RAG-Chatbot\images\logo2.jpg")
    st.image(logo, width=200)
    st.markdown("<h3 style='text-align: center; color: #ECF0F1;'>Bhaiya & Company</h3>", unsafe_allow_html=True)

# Header with background color and centered text
st.markdown(
    """
    <div style="background-color: #3a5f9e; padding: 5px;">
        <h3 style='text-align: center; color: white;'>
        Bhaiya & Company Chatbot
        </h3>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")


# Chat Interface

st.sidebar.write(f"**Selected Model:** {st.session_state.selected_model}")
st.sidebar.write(f"**Selected Prompt:** {st.session_state.selected_prompt_name}")


if st.sidebar.button("Reset Chat"):
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a button to the sidebar to start the chat
if st.sidebar.button("Start Chat", key="start"):

    st.session_state.messages = []

    # welcome message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Hello! Welcome to Bhaiya & Company Chatbot Chatbot. How can I help you with your queries today?",
        }
    )

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# Only display the chat input when the user has started the chat
if st.session_state.messages:
    if user_question := st.chat_input("Ask your question!!!"):
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]

            print("-----------------------------------")

            print("user_question", user_question)

            print("-----------------------------------")

            with st.spinner("Running..."):

                response = qa(query=user_question)

        print("response", response)

        st.write_stream(stream_data(text=response))

        st.session_state.messages.append({"role": "assistant", "content": response})



# # Fixed footer with copyright notice
# st.markdown(
#     """
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #2C3E50;
#         color: white;
#         text-align: center;
#         padding: 3px;
#     }
#     </style>
#     <div class="footer">
#         © Bhaiya & Company 2024
#     </div>
#     """, unsafe_allow_html=True
# )