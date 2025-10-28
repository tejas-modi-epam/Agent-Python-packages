
from agents.supervisor import SupervisorAgent
from agents.basic_agent import BasicAgent
from guardrails.simple_validator import validate_response
from monitor.simple_langsmith import log_interaction

def run_simple_workflow(user_query):
    log_interaction("Received user query", {"query": user_query})
    supervisor = SupervisorAgent()
    agent = BasicAgent()
    task = supervisor.assign_task(user_query)
    response = agent.handle_task(task)
    validated = validate_response(response)
    log_interaction("Workflow result", {"output": validated})
    return validated

if __name__ == "__main__":
    query = "Who was the first astronaut on the moon?"
    final = run_simple_workflow(query)
    print(final)
