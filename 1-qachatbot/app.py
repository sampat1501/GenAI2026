import streamlit as st
import groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "SIMPLE_QA_CHATBOT"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

##Prompt Template

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}"),
    ]
)


def generate_response(question, api_key, model, temprature, maxtokens):
    api_key = os.getenv("GROQ_API_KEY")
    model = ChatGroq(model="openai/gpt-oss-120b")
    outputparser = StrOutputParser()
    chain = prompt | model | outputparser
    answer = chain.invoke({"question": question})
    return answer


##Create Entire streamlit app

import streamlit as st

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(page_title="🤖 AI Assistant", page_icon="🤖", layout="wide")

# ======================================
# CUSTOM CSS
# ======================================
st.markdown(
    """
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    color: #4F46E5;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 2rem;
}

.stChatMessage {
    border-radius: 15px;
}

.metric-card {
    padding: 15px;
    border-radius: 12px;
    background-color: #f5f5f5;
}

</style>
""",
    unsafe_allow_html=True,
)

# ======================================
# HEADER
# ======================================
st.markdown("<div class='title'>🤖 AI Chat Assistant</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Powered by Groq + LangChain</div>", unsafe_allow_html=True
)

# ======================================
# SIDEBAR
# ======================================
with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg",
        width=100,
    )

    st.header("⚙️ Configuration")

    model = st.selectbox(
        "Model",
        ["openai/gpt-oss-120b", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.3)

    max_tokens = st.slider("Max Tokens", 100, 4000, 1000)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ======================================
# SESSION STATE
# ======================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================
# DISPLAY CHAT HISTORY
# ======================================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ======================================
# CHAT INPUT
# ======================================
question = st.chat_input("Ask me anything...")

if question:

    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Your Existing Function
            response = generate_response(question, None, model, temperature, max_tokens)

            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
