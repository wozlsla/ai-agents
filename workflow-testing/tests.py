import pytest
from main import graph


# 1. Full Graph
@pytest.mark.parametrize(
    "email, expected_category, expected_score",
    [
        ("this is urgent!", "urgent", 10),
        ("i wanna talk to you", "normal", 5),
        ("i have an offer for you", "spam", 1),
    ],
)
def test_full_graph(email, expected_category, expected_score):

    result = graph.invoke(
        {"email": email},
        config={
            "configurable": {
                "thread_id": "1",
            },
        },
    )

    assert result["category"] == expected_category
    assert result["priority_score"] == expected_score


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
        {"category": "spam"},
    )
    assert result["priority_score"] == 1

    # draft_response
    result = graph.nodes["draft_response"].invoke(
        {"category": "spam"},
    )
    assert "Go away" in result["response"]


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

    assert result["priority_score"] == 1


# uv run pytest tests.py -vv
