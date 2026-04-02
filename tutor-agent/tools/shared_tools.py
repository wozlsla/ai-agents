from langgraph.types import Command
from langchain_core.tools import tool


@tool
def transfer_to_agent(agent_name):
    """
    지정된 에이전트로 대화를 전달합니다.

    인자(Args):
        agent_name: 전달할 에이전트의 이름. 다음 중 하나여야 합니다: 'quiz_agent', 'teacher_agent', 'feynman_agent'
    """

    return f"{agent_name} 에이전트로 전환이 완료되었습니다."
    # return Command(
    #     goto=agent_name,
    #     graph=Command.PARENT,
    # )
