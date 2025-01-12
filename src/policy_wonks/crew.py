import os
from tabnanny import verbose
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from regex import F

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
	def economist(self) -> Agent:
		return Agent(
			allow_delegation=False,
			config=self.agents_config["economist"],
			llm=llama_instruct_model,
			tools=[search_internet],
			verbose=True,
		)

	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			allow_delegation=False,
			config=self.agents_config['financial_analyst'],
			llm=llama_instruct_model,
			tools=[search_internet],
			verbose=True,
		)

	@task
	def economist_task(self) -> Task:
		return Task(
			config=self.tasks_config['economist_task'],
			llm=gpt_4o_mini_model,
			verbose=True,
		)

	@task
	def financial_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['financial_analyst_task'],
			context=[
				self.tasks_config['economist_task'],
				],
			llm=gpt_4o_mini_model,
			verbose=True,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PolicyWonks crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			memory=True,
			planning=True,
			planning_llm=gpt_4o_mini_model,
			process=Process.sequential,
			verbose=True,
		)
