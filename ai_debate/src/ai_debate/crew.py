from crewai import Agent, Crew, Process
from crewai_tools import SerperDevTool
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class AIDebate():
    agents_config= "config/agents.yaml"

    @agent
    def proposer(self)->Agent:
        return Agent(
            config= self.agents_config['proposer'],
            verbose= true
        )
    @agent
    def opponent(self)->Agent:
        return Agent(
            config= self.agents_config['opponent'],
            verbose= True
        )
    @agent
    def judge(self)->Agent:
        return Agent(
            config= self.agents_config['judge'],
            verbose=True,
            tools=[SuperDevTool()]
        )
    @task
    def propose(self)->Task:
        return Task(
            config= self.tasks_config['propose']

        )
    @task
    def oppose(self)->Task:
        return Task(
            config= self.tasks_config['oppose']
        )
    @task
    def judging(self)->Task:
        return Task(
            config= self.tasks_config['judge']
        )
    @crew
    def crew(self)->Crew:
        return Crew(
            agents= self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
