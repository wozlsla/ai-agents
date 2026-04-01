from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
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


def make_agent(prompt, tools):

    def agent_node(state: AgentsState):
        llm_with_tools = llm.bind_tools(tools)
        response = llm_with_tools.invoke(
            f"""
            {prompt}

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

    return agent_builder.compile()


graph_builder = StateGraph(AgentsState)


def supervisor(state: AgentsState):
    structured_llm = llm.with_structured_output(SupervisorOutput)
    response = structured_llm.invoke(
        f"""
        당신은 대화를 적절한 언어 담당 상담원에게 전달(Route)하는 슈퍼바이저(Supervisor)입니다.

        고객의 요청 사항과 대화 내역을 분석하여, 다음 중 어떤 상담원이 대화를 처리해야 할지 결정하세요.

        다음에 연결할 수 있는 상담원 옵션:
        - german_agent (독일어 상담원)
        - spanish_agent (스페인어 상담원)
        - korean_agent (한국어 상담원)

        <CONVERSATION_HISTORY>
        {state.get("messages", [])}
        </CONVERSATION_HISTORY>

        **IMPORTANT**:
        - 상담원이 이미 답변을 완료했다면, __end__ 를 반환하여 대화를 종료하세요. 이 경우, 절대 계속해서 대화를 이어가지 마세요.
        """
    )

    return Command(
        goto=response.next_agent,
        update={"reasoning": response.reasoning},
    )


graph_builder.add_node(
    "supervisor",
    supervisor,
    destinations=(
        "korean_agent",
        "spanish_agent",
        "german_agent",
        END,
    ),  # for looks nice
)

graph_builder.add_node(
    "korean_agent",
    make_agent(
        prompt="당신은 한국어 전담 고객 지원 상담원입니다. 한국어로 된 문의만 처리합니다.",
        tools=[],
    ),
)
graph_builder.add_node(
    "german_agent",
    make_agent(
        prompt="당신은 독일어 전담 고객 지원 상담원입니다. 독일어로 된 문의만 처리합니다.",
        tools=[],
    ),
)
graph_builder.add_node(
    "spanish_agent",
    make_agent(
        prompt="당신은 스페인어 전담 고객 지원 상담원입니다. 스페인어로 된 문의만 처리합니다.",
        tools=[],
    ),
)

graph_builder.add_edge(START, "supervisor")
graph_builder.add_edge("korean_agent", "supervisor")
graph_builder.add_edge("german_agent", "supervisor")
graph_builder.add_edge("spanish_agent", "supervisor")

graph = graph_builder.compile()

# langsmith -> brave browser로 하지 말것.
