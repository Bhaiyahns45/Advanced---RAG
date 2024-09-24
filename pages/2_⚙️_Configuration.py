import streamlit as st
import json
from utilities.utils import stream_data, get_prompts_dict, add_prompt_to_json


# Header with background color and centered text
st.markdown(
    """
    <div style="background-color: #3a5f9e; padding: 5px;">
        <h3 style='text-align: center; color: white;'>
        Chatbot Configuration
        </h3>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")


# Sidebar with text options for user input
with st.sidebar:
    model_names = ["gpt-3.5-turbo", "gpt-4","gpt-4o","gpt-4o-mini", "gpt-4-turbo",]
    selected_model = st.selectbox("Select Model", model_names)
    api_key = st.text_input("API Key", type="password")


    st.session_state.selected_model = selected_model
    st.session_state.api_key = api_key  # Corrected


    prompts_dict = get_prompts_dict()
    prompt_names = prompts_dict.keys()

    # Initialize session state variable for storing the selected prompt
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = "gpt-3.5-turbo"

    if 'selected_prompt' not in st.session_state:
        st.session_state.selected_prompt = ""

    if 'selected_prompt_name' not in st.session_state:
        st.session_state.selected_prompt_name = ""

    # Create a select box
    selected_prompt_name = st.selectbox("Select a prompt:", prompt_names)

    # Store the selected prompt in session state
    st.session_state.selected_prompt = prompts_dict[selected_prompt_name]

    st.session_state.selected_prompt_name = selected_prompt_name


    st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)

    # Check if 'add_prompt' is in session state, initialize it if not
    if 'add_prompt' not in st.session_state:
        st.session_state.add_prompt = False

    # Button to show form
    if st.button("Add New Prompt"):
        st.session_state.add_prompt = True



st.write(f"**Selected Model:** {st.session_state.selected_model}")
st.write(f"**Selected Prompt:** {st.session_state.selected_prompt_name}")

st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)

# Show form if 'add_prompt' is True
if st.session_state.add_prompt:
    # Input fields for new prompt
    new_name = st.text_input("Enter prompt name:")
    new_prompt = st.text_area("Enter prompt text:")

    if st.button("Submit"):
        if new_name and new_prompt:
            add_prompt_to_json(new_name, new_prompt)
            st.success("Prompt added successfully! Reload the page")
            st.session_state.add_prompt = False  # Reset the form visibility
        else:
            st.error("Please provide both name and prompt text.")

