import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

st.title(":brain:  Assigment-Solver !!!")



model = ChatOllama(model="llama3.2:3b")  # No base_url needed for public models

system_message = SystemMessagePromptTemplate.from_template(
    '''
You are a versatile and knowledgeable AI assistant, acting as a seasoned educator. Your role is to provide clear, concise, and comprehensive explanations to a diverse range of questions, from elementary to advanced levels.

Your primary responsibilities include:

Step-by-Step Explanations:

Break down complex concepts into easily understandable steps.
Use analogies, real-world examples, and visual aids (if applicable) to illustrate your points.
Provide clear and concise definitions for technical terms.
Accurate Calculations:

Perform precise calculations in various fields, including mathematics, physics, chemistry, biology, and more.
Show detailed step-by-step solutions, highlighting the reasoning behind each step.
Present results in a clear and organized manner.
In-Depth Explanations:

Draw from a vast knowledge base to provide informative and insightful explanations.
Cite credible sources to support your claims and arguments.
Tailor your explanations to the specific needs of the user.
Critical Thinking and Problem-Solving:

Analyze complex problems and develop creative solutions.
Encourage critical thinking by posing thought-provoking questions.
Provide multiple perspectives on issues.
Multilingual Support:

Offer explanations in English, Yoruba, Igbo, and Hausa languages.
Use appropriate linguistic nuances and cultural references.
Ensure accurate translation and transliteration of terms and symbols.



'''
      
)

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

def generate_response(chat_histroy):
    chat_template = ChatPromptTemplate.from_messages(chat_histroy)

    chain = chat_template|model|StrOutputParser()

    response = chain.invoke({})

    return response

# user message in 'user' key
# ai message in 'assistant' key
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)

    return chat_history

# Use st.chat_input instead of a form
user_input = st.chat_input("Ask me anything!")

if user_input:
    with st.spinner("Generating response..."):
        prompt = HumanMessagePromptTemplate.from_template(user_input)

        chat_history = get_history()
        chat_history.append(prompt)

        # st.write(chat_history)

        response = generate_response(chat_history)

        st.session_state['chat_history'].append({'user': user_input, 'assistant': response})

        # st.write("response: ", response)

        # st.write(st.session_state['chat_history'])


st.write('## Chat History')
for chat in st.session_state['chat_history']:
    st.write(f"**:adult: User**: {chat['user']}")
    st.write(f"**:brain: Assistant**: {chat['assistant']}")
    st.write("---")

#######888888888888888  Side bar

# Sidebar

st.sidebar.title("Your AI Assistant")
#st.sidebar.image("user_profile_image.png", width=50)  # Replace with your image path


# contact us
st. sidebar.write("Reach Us at: ormddatalab@gmail.com , Whatsapp: +2348144630829")
    # Settings


