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

# Entrypoint for the crew
def run(policy_topic1: str, policy_topic2: str, economic_variable1: str, economic_variable2: str):
    """
    Run the crew with provided inputs.
    """
    inputs = {
        'policy_topic1': policy_topic1,
        'policy_topic2': policy_topic2,
        'economic_variable1': economic_variable1,
        'economic_variable2': economic_variable2,
    }
    # Initialize the PolicyWonks crew
    policy_wonks = PolicyWonks()
    # Run the crew and assign the output to a variable
    crew_output = policy_wonks.crew().kickoff(inputs=inputs)

     # Extract outputs from economist
    economist_task = policy_wonks.economist_task()
    economist_output = economist_task.output # get the economist output

    # Extract outputs from financial_analyst
    financial_analyst_task = policy_wonks.financial_analyst_task()
    financial_analyst_output = financial_analyst_task.output # get the financial analyst output

    # Return the outputs
    policy_wonks_output = {
        "economist_output": getattr(economist_output, 'raw', str(economist_output)),
        "financial_analyst_output": getattr(financial_analyst_output, 'raw', str(financial_analyst_output)),
    }
    return policy_wonks_output

# Define the API routes
@api.post(path='/run_crew', response_model=PolicyWonksResponse)
async def run_crew(crew_request: PolicyWonksRequest) -> PolicyWonksResponse:
    """
    Run the crew with provided input

    - **policy_topic1**: A Policy topic for Economist (e.g., fiscal policy)
    - **policy_topic2**: Policy topic for Financial Analyst (e.g., monetary policy)
    - **economic_variable1**: First economic variable to consider in the analysis (e.g., inflation rate)
    - **economic_variable2**: Second economic variable to consider in the analysis (e.g., government spending)
    """

    try:
        policy_wonks_output = run(
            crew_request.policy_topic1,
            crew_request.policy_topic2,
            crew_request.economic_variable1,
            crew_request.economic_variable2,
        )
        # Format the final answer from the Economist
        final_answer_economist = policy_wonks_output["economist_output"]
        final_answer_economist.strip("[End of Thought and Final Answer]" and "[End of Thought]" and "[Final Answer]" and "[My job depends on it!]")
        final_answer_economist.strip("I hope this analysis provides a comprehensive understanding of the current monetary policy's impact on the economy." and "If you have any further questions or need more information, please don't hesitate to ask.")

        # Format the final answer from the Financial Analyst
        final_answer_financial_analyst = policy_wonks_output["financial_analyst_output"]
        final_answer_financial_analyst.strip("[End of Thought and Final Answer]" and "[End of Thought]" and "[Final Answer]" and "[My job depends on it!]")
        final_answer_financial_analyst.strip("I hope this analysis provides a comprehensive understanding of the current monetary policy's impact on the economy." and "If you have any further questions or need more information, please don't hesitate to ask.")

        # Return the final answers as a PolicyWonksResponse object
        return PolicyWonksResponse(economist_response=final_answer_economist, financial_analyst_response=final_answer_financial_analyst)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define the root route / health-check endpoint
@api.get(path='/')
def root():
    return {
        'message': 'Welcome to the PolicyWonks API!',
        'description': 'An orchestrated, autonomous multi-agent system for analyzing economic and fiscal policy using the CrewAI framework.'
    }

# Entrypoint for the Policy Wonks API
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000, reload=True)