#!/usr/bin/env python
import sys
import warnings

from policy_wonks.crew import PolicyWonks

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'policy_topic1': 'fiscal policy',
        'policy_topic2': 'monetary policy',
        'economic_variable1': 'inflation rate',
        'economic_variable2': 'government spending',
    }
    PolicyWonks().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'policy_topic1': 'fiscal policy',
        'policy_topic2': 'monetary policy',
        'economic_variable1': 'inflation rate',
        'economic_variable2': 'government spending',
    }
    try:
        PolicyWonks().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PolicyWonks().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'policy_topic1': 'fiscal policy',
        'policy_topic2': 'monetary policy',
        'economic_variable1': 'inflation rate',
        'economic_variable2': 'government spending',
    }
    try:
        PolicyWonks().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
