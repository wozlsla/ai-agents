from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm("openai/gpt-5-nano")

agent = Agent(
    name="WeatherAgent",
    instruction="",
    model=MODEL,
)

# required(root_agent)
root_agent = agent
