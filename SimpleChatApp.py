import streamlit as st
import time


knowledge_base = {
    "Who are you?": "I am your assistant, here to help you with information or tasks.",
    "Hi":"Hey there! How may I help you?",
    "Hello":"Hello there! How may I help you?",
    "hi":"Hello there! How may I help you?",
    "hello":"Hello there! How may I help you?",
    "tell me about yourself":"I am your assistant, here to help you with information or tasks.",
    "Tell me about yourself":"I am your assistant, here to help you with information or tasks.",
    "yes":"Go ahead",
    "Yes":"Go ahead",
    "No":"Ok! Tell me if I can help you with something :)",
    "no":"Ok! Tell me if I can help you with something :)",
    
}


def response_generator(prompt):
    """Generates a response based on the prompt and knowledge base."""

    # Check for known questions in the knowledge base
    if prompt in knowledge_base:
        response = knowledge_base[prompt]
    else:
        # Handle out-of-knowledge situations
        response = "Sorry, I don't know about that yet. Can I help you with something else?"

    # Simulate typing effect with time delay
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple Chat APP")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})