My app.py Code:

import streamlit as st
from chatbot import get_response  # Import the chatbot function

# Streamlit page setup
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.text_input("You:", key="user_input")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get chatbot response
    response = get_response(user_input)
    
    # Add chatbot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(response)
