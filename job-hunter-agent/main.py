import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, task, agent, crew


@CrewBase
class JobHunterCrew:

    @agent
    def job_search_agent(self):
        return Agent(config=self.agents_config["job_search_agent"])

    @agent
    def job_matching_agent(self):
        return Agent(config=self.agents_config["job_matching_agent"])

    @agent
    def resume_optimization_agent(self):
        return Agent(config=self.agents_config["resume_optimization_agent"])

    @agent
    def company_research_agent(self):
        return Agent(config=self.agents_config["company_research_agent"])

    @agent
    def interview_prep_agent(self):
        return Agent(config=self.agents_config["interview_prep_agent"])

    @task
    def job_extraction_task(self):
        return Task(config=self.tasks_config["job_extraction_task"])

    @task
    def job_matching_task(self):
        return Task(config=self.tasks_config["job_matching_task"])

    @task
    def job_selection_task(self):
        return Task(config=self.tasks_config["job_selection_task"])

    @task
    def resume_rewriting_task(self):
        return Task(
            config=self.tasks_config["resume_rewriting_task"],
            context=[
                self.job_selection_task(),  # default. 안해도 됨.
            ],
        )

    @task
    def company_research_task(self):
        return Task(
            config=self.tasks_config["company_research_task"],
            context=[
                self.job_selection_task(),  # output 연결 (default: previous->next)
            ],
        )

    @task
    def interview_prep_task(self):
        return Task(
            config=self.tasks_config["interview_prep_task"],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ],
        )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


JobHunterCrew().crew().kickoff()
