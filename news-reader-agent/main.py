import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool


@CrewBase
class NewsReaderAgent:

    @agent
    def news_hunter_agent(self):
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            tools=[search_tool, scrape_tool],
        )

    @agent
    def summarizer_agent(self):
        return Agent(
            config=self.agents_config["summarizer_agent"],
            tools=[scrape_tool],
        )

    @agent
    def curator_agent(self):
        return Agent(config=self.agents_config["curator_agent"])

    # 작업의 결과가 자동으로 다음으로 넘어가기 때문에 순서가 중요함 (tasks.yaml)
    @task
    def content_harvesting_task(self):
        return Task(config=self.tasks_config["content_harvesting_task"])

    @task
    def summarization_task(self):
        return Task(config=self.tasks_config["summarization_task"])

    @task
    def final_report_assembly_task(self):
        return Task(config=self.tasks_config["final_report_assembly_task"])

    @crew
    def crew(self):
        return Crew(
            tasks=self.tasks,
            agents=self.agents,
            verbose=True,
        )


NewsReaderAgent().crew().kickoff(
    inputs={"topic": "National Liberation Day of Korea"},
)

# 개별 결과물에 접근
# result = NewsReaderAgent().crew().kickoff(inputs={"topic": "National Liberation Day of Korea"})

# for task_output in result.tasks_output:
#     print(task_output)
