import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.history_aware_retriever import (
    create_history_aware_retriever,
)
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

# ==================================================
# Load Environment Variables
# ==================================================

load_dotenv()

os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY", "")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Conversational QA Chatbot"

# ==================================================
# Embeddings
# ==================================================

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ==================================================
# Streamlit UI
# ==================================================

st.title("Conversational PDF Chatbot")
st.write("Upload PDF files and ask questions")

groq_api_key = st.text_input(
    "Enter Groq API Key",
    type="password",
)

if groq_api_key:

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model="openai/gpt-oss-120b",
    )

    session_id = st.text_input("Session ID", value="default_session")

    if "store" not in st.session_state:
        st.session_state.store = {}

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type="pdf",
        accept_multiple_files=True,
    )

    # ==================================================
    # Process PDFs
    # ==================================================

    if uploaded_files:

        documents = []

        for uploaded_file in uploaded_files:

            temp_pdf = "./temp.pdf"

            with open(temp_pdf, "wb") as file:
                file.write(uploaded_file.getvalue())

            loader = PyPDFLoader(temp_pdf)

            docs = loader.load()

            documents.extend(docs)

        # ==============================================
        # Split Documents
        # ==============================================

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )

        splits = text_splitter.split_documents(documents)

        # ==============================================
        # Vector Store
        # ==============================================

        vector_store = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
        )

        retriever = vector_store.as_retriever()

        # ==============================================
        # History Aware Retriever Prompt
        # ==============================================

        contextualized_q_system_prompt = """
        Given a chat history and the latest user question,
        which might reference context in the chat history,
        formulate a standalone question that can be understood
        without the chat history.

        Do not answer the question.
        Just reformulate it if needed,
        otherwise return it as is.
        """

        contextualized_q_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    contextualized_q_system_prompt,
                ),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        history_aware_retriever = create_history_aware_retriever(
            llm,
            retriever,
            contextualized_q_prompt,
        )

        # ==============================================
        # Question Answer Prompt
        # ==============================================

        system_prompt = """
        You are an assistant for question-answering tasks.

        Use the following pieces of retrieved context
        to answer the question.

        If you don't know the answer,
        say that you don't know.

        Use a maximum of 3 sentences
        and keep the answer concise.

        {context}
        """

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(
            llm,
            qa_prompt,
        )

        # ==============================================
        # RAG Chain
        # ==============================================

        rag_chain = create_retrieval_chain(
            history_aware_retriever,
            question_answer_chain,
        )

        # ==============================================
        # Session History
        # ==============================================

        def get_session_history(
            session_id: str,
        ) -> BaseChatMessageHistory:

            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()

            return st.session_state.store[session_id]

        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

        # ==============================================
        # Chat Input
        # ==============================================

        user_input = st.text_input("Ask a question")

        if user_input:

            session_history = get_session_history(session_id)

            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}},
            )

            st.success(f"Assistant: {response['answer']}")

            st.write(
                "Chat History:",
                session_history.messages,
            )

else:
    st.warning("Please enter your Groq API Key.")
