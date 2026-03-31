from typing import Literal, List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain.chat_models import init_chat_model


llm = init_chat_model("openai:gpt-5-nano")

checkpointer = MemorySaver()


class EmailState(TypedDict):

    email: str
    category: Literal["spam", "normal", "urgent"]
    priority_score: int
    response: str


class EmailClassificationOutput(BaseModel):

    category: Literal["spam", "normal", "urgent"] = Field(
        description="Category of the email",
    )


class PriorityScoreOutput(BaseModel):

    priority_score: int = Field(
        description="Priority score from 1 to 10",
        ge=1,
        le=10,
    )


def categorize_email(state: EmailState):

    s_llm = llm.with_structured_output(EmailClassificationOutput)

    result = s_llm.invoke(
        f"""이 이메일을 다음 세 가지 카테고리 중 하나로 분류해 주세요:
        - urgent: 시간이 촉박하거나 즉각적인 주의가 필요한 경우
        - normal: 일반적인 업무 관련 커뮤니케이션
        - spam: 홍보, 마케팅 또는 원치 않는 콘텐츠

        Email: {state["email"]}"""
    )

    return {
        "category": result.category,
    }


def assign_priority(state: EmailState):

    s_llm = llm.with_structured_output(PriorityScoreOutput)

    result = s_llm.invoke(
        f"""이 {state["category"]} 이메일에 대해 1~10점 사이의 우선순위 점수를 부여해 주세요.

        Consider:
        - Category: {state["category"]}
        - Email content: {state["email"]}

        Guidelines:
        - Urgent 이메일: 보통 8-10점
        - Normal 이메일: 보통 4-7점
        - Spam 이메일: 보통 1-3점"""
    )

    return {
        "priority_score": result.priority_score,
    }


def draft_response(state: EmailState) -> EmailState:
    result = llm.invoke(
        f"""이 {state['category']} 이메일에 대해 짧고 전문적인 응답 초안을 작성하세요.

        Original email: {state['email']}
        Category: {state['category']}
        Priority: {state['priority_score']}/10

        Guidelines:
        - Urgent: 긴급함을 인지했음을 알리고, 즉각적인 처리를 약속할 것
        - Normal: 전문적인 확인 메시지와 표준 처리 기한을 안내할 것
        - Spam: 메시지가 필터링되었음을 알리는 간결한 통보

        응답은 2문장 이내로 작성하세요."""
    )
    return {
        "response": result.content,
    }


graph_builder = StateGraph(EmailState)


graph_builder.add_node("categorize_email", categorize_email)
graph_builder.add_node("assign_priority", assign_priority)
graph_builder.add_node("draft_response", draft_response)

graph_builder.add_edge(START, "categorize_email")
graph_builder.add_edge("categorize_email", "assign_priority")
graph_builder.add_edge("assign_priority", "draft_response")
graph_builder.add_edge("draft_response", END)

graph = graph_builder.compile(checkpointer=checkpointer)
