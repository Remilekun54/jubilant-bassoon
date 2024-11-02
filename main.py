import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

st.title(":brain:  Assignment Solver !!!")


@st.cache(allow_output_mutation=True)
def get_model():
  """Initializes and caches the ChatOllama model."""
  return ChatOllama(model="llama3.2:3b")  # No base_url needed for public models


def generate_response(chat_history):
  """Generates response based on chat history and returns it."""
  chat_template = ChatPromptTemplate.from_messages(chat_history)
  chain = chat_template | model | StrOutputParser()
  response = chain.invoke({})
  return response


# user message in 'user' key
# ai message in 'assistant' key
def get_history():
  """Retrieves chat history from session state."""
  chat_history = [system_message]
  for chat in st.session_state.get("chat_history", []):
    prompt = HumanMessagePromptTemplate.from_template(chat["user"])
    chat_history.append(prompt)

    ai_message = AIMessagePromptTemplate.from_template(chat["assistant"])
    chat_history.append(ai_message)

  return chat_history


# Use st.chat_input instead of a form
user_input = st.chat_input("Ask me anything!")

model = get_model()  # Initialize model outside user interaction

if user_input:
  with st.spinner("Generating response..."):
    prompt = HumanMessagePromptTemplate.from_template(user_input)

    chat_history = get_history()
    chat_history.append(prompt)

    response = generate_response(chat_history)

    st.session_state["chat_history"].append({"user": user_input, "assistant": response})


st.write('## Chat History')
for chat in st.session_state.get("chat_history", []):
  st.write(f"**:adult: User**: {chat['user']}")
  st.write(f"**:brain: Assistant**: {chat['assistant']}")
  st.write("---")


#######888888888888888  Side bar

# Sidebar

st.sidebar.title("Your AI Assistant")
# st.sidebar.image("user_profile_image.png", width=50)  # Replace with your image path

# contact us
st.sidebar.write("Reach Us at: ormddatalab@gmail.com , Whatsapp: +2348144630829")
