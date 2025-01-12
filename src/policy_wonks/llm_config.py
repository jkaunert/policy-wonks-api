import os
from crewai import LLM


jamba_1_5_mini_model = LLM(
	model="azure/AI21-Jamba-1.5-Mini",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)

jamba_1_5_large_model = LLM(
	model="openai/AI21-Jamba-1.5-Large",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)

llama_instruct_model = LLM(
	model="openai/Llama-3.3-70B-Instruct",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)

gpt_4o_mini_model = LLM(
	model="azure/gpt-4o-mini",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)

gpt_4o_model = LLM(
	model="openai/gpt-4o",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)