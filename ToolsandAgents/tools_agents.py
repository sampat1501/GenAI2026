##Arxiv
## Tools creation
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper

##Create API wrappers - this is inbuild wiki tool

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
wiki.name

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
arxiv.name

tools = [wiki, arxiv]


##Custom tools
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.tools import create_retriever_tool

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_NAME"] = "Tools_And_Agents"

## groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key=groq_api_key, model="openai/gpt-oss-120b")

# Create Emmbedings model
embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
# Document Chunking and splitting
loader = WebBaseLoader("https://aws.amazon.com/what-is/large-language-model/")
docs = loader.load()
spliter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=300)
documents = spliter.split_documents(docs)

##Create Vectorstore
vector_store = FAISS.from_documents(documents=documents, embedding=embeddings)
retriever = vector_store.as_retriever()
## Create retriver tool

retriever_tool = create_retriever_tool(
    retriever,
    "aws_llm_retriever",
    "Search the AWS article about large language models.",
)
tools.append(retriever_tool)
##Create Prompt template
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Use the provided tools when needed.",
        ),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
print(prompt)


##Agents
from langchain_classic.agents import create_openai_functions_agent

agent = create_openai_functions_agent(llm=model, tools=tools, prompt=prompt)
## Agent executor
from langchain_classic.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

##Unable to proceed beacuase of Open AI API key error
