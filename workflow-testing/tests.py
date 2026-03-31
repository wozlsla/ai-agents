import dotenv

dotenv.load_dotenv()

import pytest
from main import graph
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model


llm = init_chat_model("openai:gpt-5-nano")


class SimilarityScoreOutput(BaseModel):

    similarity_score: int = Field(
        description="이 응답이 예시들과 얼마나 유사합니까?",
        gt=0,
        lt=100,
    )


RESPONSE_EXAMPLES = {
    "urgent": [
        "긴급 메시지를 확인했습니다. 즉시 검토 중이며 가능한 한 빨리 회신드리겠습니다.",
        "긴급 요청을 접수하여 우선적으로 처리하고 있습니다. 저희 팀이 바로 확인 중입니다.",
        "해당 긴급 사안을 즉각 확인하고 있습니다. 신속하게 답변드리겠습니다.",
    ],
    "normal": [
        "이메일 감사합니다. 내용을 검토한 후 24~48시간 이내에 회신드리겠습니다.",
        "메시지를 정상적으로 접수했으며 곧 답변드리겠습니다. 연락 주셔서 감사합니다.",
        "문의해 주셔서 감사합니다. 요청 사항을 처리한 후 곧 연락드리겠습니다.",
        "업데이트해 주셔서 감사합니다. 내용을 검토한 후 필요한 경우 후속 조치를 취하겠습니다.",
        "프로젝트 진행 상황을 공유해 주셔서 감사합니다. 검토 후 이번 주말까지 후속 답변을 드리겠습니다.",
        "업데이트 사항을 공유해 주셔서 감사합니다. 검토 후 그에 맞게 답변드리겠습니다.",
    ],
    "spam": [
        "이 메시지는 스팸으로 분류되어 필터링되었습니다.",
        "이 이메일은 홍보용 콘텐츠로 식별되었습니다.",
        "이 메시지는 스팸으로 표시되었습니다.",
    ],
}


def judge_response(response: str, category: str):

    s_llm = llm.with_structured_output(SimilarityScoreOutput)

    examples = RESPONSE_EXAMPLES[category]
    result = s_llm.invoke(
        f"""
        이 응답이 제공된 예시들과 얼마나 유사한지 점수를 매기세요.

        Category: {category}

        Examples:
        {"\n".join(examples)}

        Response to evaluate:
        {response}

        Scoring criteria:
        - 90-100: 어조, 내용, 의도가 매우 유사함
        - 70-89: 약간의 차이가 있으나 유사함
        - 50-69: 보통 수준의 유사함, 주요 아이디어를 잘 포착함
        - 30-49: 어느 정도 유사하지만 핵심 요소가 누락됨
        - 0-29: 매우 다르거나 부적절함
        """
    )

    return result.similarity_score


# 1. Full Graph
@pytest.mark.parametrize(
    "email, expected_category, min_score, max_score",
    [
        ("this is urgent!", "urgent", 8, 10),
        ("i wanna talk to you", "normal", 4, 7),
        ("i have an offer for you", "spam", 1, 3),
    ],
)
def test_full_graph(email, expected_category, min_score, max_score):

    result = graph.invoke(
        {"email": email},
        config={
            "configurable": {
                "thread_id": "1",
            },
        },
    )

    assert result["category"] == expected_category
    assert min_score <= result["priority_score"] <= max_score


# 2. Individual node
def test_individual_nodes():
    # node의 이름으로 node를 참고 가능

    # categorize_email
    result = graph.nodes["categorize_email"].invoke(
        {"email": "check out this offer"},
    )
    assert result["category"] == "spam"

    # assign_priority
    result = graph.nodes["assign_priority"].invoke(
        {"category": "spam", "email": "buy this pot."},
    )
    assert 1 <= result["priority_score"] <= 3

    # draft_response
    result = graph.nodes["draft_response"].invoke(
        {
            "category": "spam",
            "email": "빨리 부자가 되세요!!! 당신을 위한 다단계 사업이 있습니다",
            "priority_score": 1,
        },
    )

    similarity_score = judge_response(result["response"], "spam")
    assert similarity_score >= 70


# 3. Partial node
def test_partial_execution():
    # checkpointer 필요 -> graph의 state 저장

    graph.update_state(
        config={
            "configurable": {
                "thread_id": "1",
            },
        },
        values={
            "email": "이 제안을 확인해 보세요.",
            "category": "spam",
        },
        as_node="categorize_email",  # like pretend
    )

    result = graph.invoke(
        None,
        config={
            "configurable": {
                "thread_id": "1",
            },
        },
        # interrupt_before=
        interrupt_after="draft_response",
    )

    assert 1 <= result["priority_score"] <= 3
