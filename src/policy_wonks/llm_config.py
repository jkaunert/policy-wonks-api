import os
from crewai import LLM

hf_qwq_model = LLM(
    model="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

jamba_1_5_mini_model = LLM(
	model="azure/AI21-Jamba-1.5-Mini",
	api_key=os.getenv("GITHUB_API_KEY"),
	base_url="https://models.inference.ai.azure.com",
)

together_ai_llama3_3 = LLM(
	model="openai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
	api_key=os.getenv("TOGETHERAI_API_KEY"),
    temperature=0.7,
    top_p=0.7,
    stop=["<|eot_id|>","<|eom_id|>"],
	base_url="https://api.together.xyz/v1",
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