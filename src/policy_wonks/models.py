from pydantic import BaseModel, Field

class PolicyWonksRequest(BaseModel):
    policy_topic1: str = Field(default="fiscal policy")
    policy_topic2: str = Field(default="monetary policy")
    economic_variable1: str = Field(default="inflation rate")
    economic_variable2: str = Field(default="government spending")

class PolicyWonksResponse(BaseModel):
    economist_response: str
    financial_analyst_response: str