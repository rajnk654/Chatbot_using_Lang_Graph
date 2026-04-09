<<<<<<< HEAD
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread_1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Load the conversation history

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.text_input('Type your message here...')

if user_input:
    
    # First append the user message to the message history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
        
    
    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    ai_message = response['messages'][-1].content
    # Here you would call your chatbot function and get the response
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)

=======
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread_1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Load the conversation history

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.text_input('Type your message here...')

if user_input:
    
    # First append the user message to the message history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
        
    
    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    ai_message = response['messages'][-1].content
    # Here you would call your chatbot function and get the response
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)

>>>>>>> 6cdb671 (Remove .venv)
