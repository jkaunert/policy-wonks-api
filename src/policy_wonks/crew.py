from crewai import (
	Agent,
	Crew,
	Process,
	Task,
)
from crewai.project import (
	CrewBase,
	agent,
	crew,
	task,
)
from crewai_tools import (
	SerperDevTool,
	WebsiteSearchTool,
)
from policy_wonks.llm_config import (
	jamba_1_5_mini_model,
	jamba_1_5_large_model,
	llama_instruct_model,
	gpt_4o_mini_model,
	gpt_4o_model,
)

@CrewBase
class PolicyWonks():
	"""PolicyWonks crew"""

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	@agent
	def economist(self) -> Agent:
		return Agent(
			config=self.agents_config["economist"],
			llm=gpt_4o_mini_model,
			tools=[
				WebsiteSearchTool(),
				SerperDevTool(),
			],
			verbose=True,
		)

	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config["financial_analyst"],
			llm=gpt_4o_mini_model,
			tools=[
				WebsiteSearchTool(),
				SerperDevTool(),
			],
			verbose=True,
		)

	@task
	def economist_task(self) -> Task:
		return Task(
			config=self.tasks_config["economist_task"],
		)

	@task
	def financial_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config["financial_analyst_task"],
			context=[
				self.tasks_config["economist_task"],
				],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PolicyWonks crew"""

		return Crew(
			agents=self.agents,
			function_calling_llm=jamba_1_5_mini_model,
			memory=True,
			planning=True,
			planning_llm=llama_instruct_model,
			process=Process.sequential,
			tasks=self.tasks,
			verbose=True,
		)
