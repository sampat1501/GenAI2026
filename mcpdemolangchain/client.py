from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.shared.context import RequestContext as MCPRequestContext
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.documents.base import Blob
from mcp.client.streamable_http import streamable_http_client
import os
from dotenv import load_dotenv

load_dotenv()
import asyncio

groq_api_key = os.getenv("GROQ_API_KEY")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  ##Ensure correct absolute path
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamablehttp_client",
            },
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")

    ##Create Agent

    agent = create_react_agent(model=model, tools=tools)

    math_response = await agent.invoke(
        {"messages": {"role": "user", "content": "whats(3+5)*12?"}}
    )

    print(math_response["messages"][-1].content)

    asyncio.run(main())
