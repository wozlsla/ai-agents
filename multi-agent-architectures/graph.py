from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import InjectedState, ToolNode, tools_condition
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from pydantic import BaseModel


class SupervisorOutput(BaseModel):

    next_agent: Literal["korean_agent", "german_agent", "spanish_agent", "__end__"]
    reasoning: str


class AgentsState(MessagesState):
    current_agent: str
    transfered_by: str
    reasoning: str


# llm = init_chat_model("openai:gpt-5-nano") # 안됨
llm = init_chat_model("openai:gpt-4o")


def make_agent_tool(tool_name, tool_description, system_prompt, tools):

    def agent_node(state: AgentsState):
        llm_with_tools = llm.bind_tools(tools)
        response = llm_with_tools.invoke(
            f"""
            {system_prompt}

            Conversation History:
            {state["messages"]}
            """
        )
        return {"messages": [response]}

    agent_builder = StateGraph(AgentsState)

    agent_builder.add_node("agent", agent_node)
    agent_builder.add_node(
        "tools",
        ToolNode(tools=tools),
    )

    agent_builder.add_edge(START, "agent")
    agent_builder.add_conditional_edges("agent", tools_condition)
    agent_builder.add_edge("tools", "agent")
    agent_builder.add_edge("agent", END)

    # return agent_builder.compile()
    agent = agent_builder.compile()

    @tool(name_or_callable=tool_name, description=tool_description)
    def agent_tool(state: Annotated[dict, InjectedState]):
        result = agent.invoke(state)
        return result["messages"][-1].content

    return agent_tool


graph_builder = StateGraph(AgentsState)


tools = [
    make_agent_tool(
        tool_name="korean_agent",
        tool_description="사용자가 한국어로 말할 때 이 도구를 사용하세요",
        system_prompt="당신은 한국어 고객 지원 상담원입니다. 한국어로 답변하세요.",
        tools=[],
    ),
    make_agent_tool(
        tool_name="spanish_agent",
        tool_description="사용자가 스페인어로 말할 때 이 도구를 사용하세요",
        system_prompt="당신은 스페인어 고객 지원 상담원입니다. 스페인어로 답변하세요.",
        tools=[],
    ),
    make_agent_tool(
        tool_name="greek_agent",
        tool_description="사용자가 그리스어로 말할 때 이 도구를 사용하세요",
        system_prompt="당신은 그리스어 고객 지원 상담원입니다. 그리스어로 답변하세요.",
        tools=[],
    ),
]


def supervisor(state: AgentsState):
    llm_with_tools = llm.bind_tools(tools=tools)
    result = llm_with_tools.invoke(state["messages"])
    return {
        "messages": [result],
    }


graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", ToolNode(tools=tools))

graph_builder.add_edge(START, "supervisor")
graph_builder.add_conditional_edges("supervisor", tools_condition)
graph_builder.add_edge("tools", "supervisor")
graph_builder.add_edge("supervisor", END)

graph = graph_builder.compile()
