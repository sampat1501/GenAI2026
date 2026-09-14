import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_PROJECT"] = "GROQ_QA_CHATBOT"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
groq_api_key = os.getenv("GROQ_API_KEY")

##
llm_model = ChatGroq(groq_api_key=groq_api_key, model="openai/gpt-oss-120b")


prompt = ChatPromptTemplate.from_template("""
    Answer the questions based only on the provided context.
    Please provide the most accurate response.

    <context>
    {context}
    </context>

    Question: {input}
    """)


def create_vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        st.session_state.loader = PyPDFDirectoryLoader("Researchpapers")
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        st.session_state.final_document = (
            st.session_state.text_splitter.split_documents(st.session_state.documents)
        )

        st.session_state.vectors = FAISS.from_documents(
            st.session_state.final_document, st.session_state.embeddings
        )


user_prompt = st.text_input("Enter your query from the the research paper")

if st.button("Document Embeddings"):
    create_vector_embeddings()
    st.write("vector Database is ready")


import time

if user_prompt and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm_model, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retriever_chain.invoke({"input": user_prompt})
    print(f"Response time: {time.process_time()-start}")
    st.write(response["answer"])

    ##With streamlit expander

    with st.expander("Document simmilarity search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------------------------")
