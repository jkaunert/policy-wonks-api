import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.tasks.task_output import TaskOutput

load_dotenv()

search_internet = SerperDevTool()

llama_instruct_model = LLM(
	model='openai/Llama-3.3-70B-Instruct',
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url='https://models.inference.ai.azure.com',
)

gpt_4o_mini_model = LLM(
	model='gpt-4o-mini',
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url='https://models.inference.ai.azure.com',
)
@CrewBase
class PolicyWonks():
	"""PolicyWonks crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config[''],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config[''],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config[''],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config[''],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PolicyWonks crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
