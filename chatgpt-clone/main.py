import dotenv

dotenv.load_dotenv()

import asyncio
import streamlit as st
from agents import Agent, Runner, SQLiteSession, WebSearchTool


# Agent
if "agent" not in st.session_state:
    st.session_state["agent"] = Agent(
        name="ChatGPT Clone",
        instructions="""
        You are a helpful assistant.
 
        You have access to the followig tools:
            - Web Search Tool: Use this when the user asks a questions that isn't in your training data. Use this tool when the users asks about current or future events, when you think you don't know the answer, try searching for it in the web first.
        """,
        tools=[WebSearchTool()],
    )

agent = st.session_state["agent"]


# Session 초기화
if "session" not in st.session_state:
    st.session_state["session"] = SQLiteSession(
        "chat-history",  # ession id
        "chat-gpt-clone-memory.db",  # .db path
    )

session = st.session_state["session"]


async def paint_history():
    messages = await session.get_items()

    for message in messages:

        if "role" in message:
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.write(message["content"])
                elif message["type"] == "message":
                    st.write(message["content"][0]["text"])

        if "type" in message and message["type"] == "web_search_call":
            with st.chat_message("ai"):
                st.write("Searching Web...")


def update_status(status_container, event):

    # just for web search tool
    status_messages = {
        "response.web_search_call.completed": ("✅ Web search completed.", "complete"),
        "response.web_search_call.in_progress": (
            "🔍 Starting web search...",
            "running",
        ),
        "response.web_search_call.searching": (
            "🔍 Web search in progress...",
            "running",
        ),
        "response.completed": (" ", "complete"),
    }

    if event in status_messages:
        label, state = status_messages[event]
        status_container.update(label=label, state=state)


# Draw UI
asyncio.run(paint_history())


# Runner
async def run_agent(message):
    with st.chat_message("ai"):
        status_container = st.status("⏳", expanded=False)
        text_placeholder = st.empty()
        response = ""

        stream = Runner.run_streamed(agent, message, session=session)

        async for event in stream.stream_events():
            if event.type == "raw_response_event":

                update_status(status_container, event.data.type)

                if event.data.type == "response.output_text.delta":
                    response += event.data.delta
                    text_placeholder.write(response)


### UI ###

prompt = st.chat_input("Write a message for your assistant")

if prompt:
    with st.chat_message("human"):
        st.write(prompt)

    asyncio.run(run_agent(prompt))

with st.sidebar:

    reset = st.button("Reset Memory")
    if reset:
        asyncio.run(session.clear_session())

    st.write(asyncio.run(session.get_items()))
