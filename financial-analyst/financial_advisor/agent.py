from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm("openai/gpt-5-nano")


def get_weather(city: str):
    return f"The weather in {city} is 30 degrees."


def convert_units(degrees: int):
    return f"That is 40 farenheit"


geo_agent = Agent(
    name="GeoAgent",
    instruction="You help with geo questions",
    model=MODEL,
    description="Transfer to this agent when you have a geo related question.",
)


agent = Agent(
    name="WeatherAgent",
    instruction="",
    model=MODEL,
    tools=[
        get_weather,
        convert_units,
    ],
    sub_agents=[
        geo_agent,
    ],
)

# required(root_agent)
root_agent = agent
