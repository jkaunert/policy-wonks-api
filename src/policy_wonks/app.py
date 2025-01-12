import os, sys, uvicorn, warnings
from crewai import Task
from crewai.tasks.task_output import TaskOutput
from fastapi import (
    FastAPI,
    HTTPException,
)
from policy_wonks.crew import PolicyWonks
from policy_wonks.models import (
    PolicyWonksRequest,
    PolicyWonksResponse,
)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Initialize FastAPI
api =  FastAPI(
    title='Policy Wonks API',
    description="""
        API for Policy Wonks - an orchestrated, autonomous multi-agent system
        for analyzing economic and fiscal policy using the CrewAI framework.
    """,
    version='0.1.0',
)

# Define the API routes
@api.post(path='/run_crew', response_model=PolicyWonksResponse)
async def run_crew(request: PolicyWonksRequest) -> PolicyWonksResponse:
       """
    Run the crew with provided variables.

    - **policy_topic1**: A Policy topic for Economist (e.g., fiscal policy)
    - **policy_topic2**: Policy topic for Financial Analyst (e.g., monetary policy)
    - **economic_variable1**: First economic variable to consider in the analysis (e.g., inflation rate)
    - **economic_variable2**: Second economic variable to consider in the analysis (e.g., government spending)
    """
       pass

@api.get(path='/')
def root():
    return {
        'message': 'Welcome to the PolicyWonks API!',
        'description': 'An orchestrated, autonomous multi-agent system for analyzing economic and fiscal policy using the CrewAI framework.'
    }

# Entrypoint for the Policy Wonks API
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000, reload=True)