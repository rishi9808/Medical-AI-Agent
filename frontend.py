# 1. setup streamlit
import streamlit as st
import requests

st.set_page_config(
    page_title="Medical AI Agent",
    page_icon=":guardsman:",
    layout="wide"
)
st.title("Medical AI Agent")

# 2. define backend URL
BACKEND_URL = "http://localhost:8000/query"

# 2. initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 3 chat input
user_input = st.chat_input("Whats on your mind?")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # send query to backend
    response = requests.post(BACKEND_URL, json={"message": user_input})
    

    # check if response is successful
    if response.status_code == 200:
        fixed_response = response.json().get("message", "No response from backend")
    else:
        fixed_response = f"Error: {response.status_code} - {response.text}"

    # fixed_response= "test dummy response"
    st.session_state.chat_history.append({ "role": "assistant", "content": fixed_response})

# 4. show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])