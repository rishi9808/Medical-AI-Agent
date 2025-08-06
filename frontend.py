# 1. setup streamlit
import streamlit as st

st.set_page_config(
    page_title="Medical AI Agent",
    page_icon=":guardsman:",
    layout="wide"
)
st.title("Medical AI Agent")

# 2. initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 3 chat input
user_input = st.chat_input("Whats on your mind?")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    fixed_response= "test dummy response"
    st.session_state.chat_history.append({ "role": "assistant", "content": fixed_response})

# 4. show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])