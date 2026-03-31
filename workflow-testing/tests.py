import dotenv

dotenv.load_dotenv()

import pytest
from main import graph


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
    # result = graph.nodes["draft_response"].invoke(
    #     {"category": "spam"},
    # )
    # assert "Go away" in result["response"]


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
            "email": "please check out this offer",
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
