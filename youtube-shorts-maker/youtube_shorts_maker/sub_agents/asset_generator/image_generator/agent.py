from google.adk.agents import SequentialAgent
from .prompt_builder.agent import prompt_builder_agent

image_generator_agent = SequentialAgent(
    name="ImageGeneratorAgent",
    description="Generates images for the YouTube Short",
    sub_agents=[
        prompt_builder_agent,
    ],
)
