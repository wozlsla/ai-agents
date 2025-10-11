from google.adk.agents import Agent
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm
from .sub_agents.data_analyst import data_analyst
from .sub_agents.financial_analyst import financial_analyst
from .sub_agents.news_analyst import news_analyst
from .prompt import PROMPT

MODEL = LiteLlm("openai/gpt-5-nano")


def save_advice_report(tool_context: ToolContext, summary: str):
    # save_advice_report 는 일반 tool과 같음. 원한다면 ToolContext 받게해 사용 가능.
    # ToolContext: 현재 에이전트의 실행 환경에 대한 정보를 담고 있으며, state는 현재 에이전트 세션의 저장소 역할

    # ToolContext 객체의 state 할당
    state = tool_context.state

    data_analyst_result = state.get("data_analyst_result")
    financial_analyst_result = state.get("financial_analyst_result")
    news_analyst_result = state.get("news_analyst_result")

    report = f"""
        # Excetuve Summary and Advice:
        {summary}

        ## Data Analyst Report:
        {data_analyst_result}

        ## Financial Analyst Report:
        {financial_analyst_result}
        
        ## News Analyst Report:
        {news_analyst_result}
        """

    # state에 저장
    state["report"] = report

    return {
        "success": True,
    }


financial_advisor = Agent(
    name="FinancialAdvisor",
    instruction=PROMPT,
    model=MODEL,
    tools=[
        AgentTool(agent=financial_analyst),
        AgentTool(agent=news_analyst),
        AgentTool(agent=data_analyst),
        save_advice_report,
    ],
)

# required(root_agent)
root_agent = financial_advisor
