from dotenv import load_dotenv
from pydantic_ai.agent import Agent

load_dotenv()

def create_agent(model: str, prompt: str) -> Agent: 
    agent: Agent = Agent(model=model, system_prompt=prompt)
    return agent

agent = create_agent('groq:gemma2-9b-it', 'You is powerfull assitante for task life')
result = agent.run_sync('Hello')
print(result.data)