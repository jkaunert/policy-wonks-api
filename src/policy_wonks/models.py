from pydantic import BaseModel, Field

class PolicyWonksRequest(BaseModel):
    policy_topic1: str = Field(default="fiscal policy", description="The policy topic for the Economist to focus on")
    policy_topic2: str = Field(default="monetary policy", description="The policy topic for the Financial Analyst to focus on")
    economic_variable1: str = Field(default="inflation rate", description="The first economic variable for both agents to consider")
    economic_variable2: str = Field(default="government tariffs", description="The second economic variable for both agents to consider")

class PolicyWonksResponse(BaseModel):
    economist_response: str = Field(description="Response from the economist")
    financial_analyst_response: str = Field(description="Response from the financial analyst")