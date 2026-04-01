from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage
from langchain.chat_models import init_chat_model


class AgentsState(MessagesState):
    current_agent: str
    transfered_by: str


llm = init_chat_model("openai:gpt-5-nano")


def make_agent(prompt, tools, language):

    def agent_node(state: AgentsState):
        llm_with_tools = llm.bind_tools(tools)
        system = SystemMessage(
            content=(
                f"{prompt}\n\n"
                "규칙:\n"
                f"1. 고객의 메시지가 {language}가 아니면, 반드시 handoff_tool을 호출하여 해당 언어의 상담원에게 전달하세요.\n"
                f"2. {language}가 아닌 메시지에는 절대 직접 응답하지 마세요. 텍스트 응답 없이 handoff_tool만 호출하세요.\n"
                f"3. {language} 메시지에만 직접 응답하세요."
            )
        )
        response = llm_with_tools.invoke([system] + state["messages"])
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
    # agent_builder.add_edge("agent", END)

    return agent_builder.compile()


@tool
def handoff_tool(transfer_to: str, transfered_by: str):
    """
    다른 상담원에게 연결(Handoff)합니다.
    고객이 현재 상담원의 담당 언어가 아닌 다른 언어로 말할 때 이 도구를 사용하세요.

    `transfer_to`에 가능한 값:
    - `korean_agent` (한국어 상담원)
    - `german_agent` (독일어 상담원)
    - `spanish_agent` (스페인어 상담원)

    `transfered_by`에 가능한 값:
    - `korean_agent`
    - `german_agent`
    - `spanish_agent`

    인자(Args):
        transfer_to: 대화를 전달받을 상담원
        transfered_by: 대화를 전달한 상담원
    """
    if transfer_to == transfered_by:
        return {
            "error": "Stop trying to transfer to yourself and answer the question or i will fire you."
        }

    return Command(
        update={
            "current_agent": transfer_to,
            "transfered_by": transfered_by,
        },
        goto=transfer_to,
        graph=Command.PARENT,
    )


graph_builder = StateGraph(AgentsState)

graph_builder.add_node(
    "korean_agent",
    make_agent(
        prompt="당신은 한국어 전담 고객 지원 상담원입니다. 한국어로 된 문의만 처리합니다.",
        tools=[handoff_tool],
        language="한국어",
    ),
    destinations=("german_agent", "spanish_agent"),
)
graph_builder.add_node(
    "german_agent",
    make_agent(
        prompt="당신은 독일어 전담 고객 지원 상담원입니다. 독일어로 된 문의만 처리합니다.",
        tools=[handoff_tool],
        language="독일어",
    ),
    destinations=("korean_agent", "spanish_agent"),
)
graph_builder.add_node(
    "spanish_agent",
    make_agent(
        prompt="당신은 스페인어 전담 고객 지원 상담원입니다. 스페인어로 된 문의만 처리합니다.",
        tools=[handoff_tool],
        language="스페인어",
    ),
    destinations=("german_agent", "korean_agent"),
)

graph_builder.add_edge(START, "korean_agent")

graph = graph_builder.compile()

# langsmith -> brave browser로 하지 말것.
