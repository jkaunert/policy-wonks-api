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

@api.get(path='/')
def root():
    return {
        'message': 'Welcome to the Policy Wonks API!'
    }

# Entrypoint for the Policy Wonks API
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000, reload=True)