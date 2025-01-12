import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, RagTool

load_dotenv()

# tools
search_internet = SerperDevTool()

# llms
jamba_1_5_mini_model = LLM(
	model='openai/AI21-Jamba-1.5-Mini',
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url='https://models.inference.ai.azure.com',
)

llama_instruct_model = LLM(
	model='openai/Meta-Llama-3-70B-Instruct',
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url='https://models.inference.ai.azure.com',
)

gpt_4o_mini_model = LLM(
	model='openai/gpt-4o-mini',
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
			memory=True,
			tools=[search_internet, RagTool()],
			verbose=True,
		)

	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			allow_delegation=False,
			config=self.agents_config['financial_analyst'],
			llm=llama_instruct_model,
			memory=True,
			tools=[search_internet, RagTool()],
			verbose=True,
		)

	@task
	def economist_task(self) -> Task:
		return Task(
			config=self.tasks_config['economist_task'],
			verbose=True,
		)

	@task
	def financial_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['financial_analyst_task'],
			context=[
				self.tasks_config['economist_task'],
				],
			verbose=True,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PolicyWonks crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			planning=True,
			memory=True,
			planning_llm=llama_instruct_model,
			function_calling_llm=gpt_4o_mini_model,
			process=Process.sequential,
			verbose=True,
		)
