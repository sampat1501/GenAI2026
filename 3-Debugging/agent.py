from typing import Annotated
from typing_extensions import TypedDict
from langchain_groq import ChatGroq
from langgraph.graph import START, END
from langgraph.graph.message import add_messages
from langgraph.graph.state import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

model = init_chat_model("openai/gpt-oss-120b", model_provider="GROQ")
model
##Langsmit API KEY
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "TestProject"

##Create Stategraph


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


##Graph with tool call


def make_tool_graph():
    ##Graph with tool call
    from langchain_core.tools import tool

    @tool
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b

    tool_node = ToolNode([add])
    tools = [add]
    llm_with_tool = model.bind_tools([add])

    def call_llm_model(state: State):
        return {"messages": [llm_with_tool.invoke(state["messages"])]}

    ##Build the graph with StateGrapgh
    builder = StateGraph(State)

    ##Build Nodes - 1st node always llm call
    builder.add_node("call_llm_model", call_llm_model)
    builder.add_node("tools", ToolNode(tools))

    ## Add Edges

    builder.add_edge(START, "call_llm_model")
    builder.add_conditional_edges("call_llm_model", tools_condition)
    builder.add_edge("tools", "call_llm_model")

    ##Compile the graph and Show the tool
    graph = builder.compile()

    ##Display graph
    from IPython.display import Image, display

    display(Image(graph.get_graph().draw_mermaid_png()))
    return graph


tool_agent = make_tool_graph()
