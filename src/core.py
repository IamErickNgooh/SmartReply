from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.messages import ModelMessage

load_dotenv()

def create_agent(model: str, prompt: str) -> Agent: 
    agent: Agent = Agent(model=model, system_prompt=prompt)
    return agent

store: dict[str, list[bytes]] = {}

def create_session_if_not_exists(session_id: str) -> None:
    if session_id not in store:
        store[session_id]: list[ModelMessage] = [] # type: ignore

    
#agent = create_agent('groq:gemma2-9b-it', 'You is powerfull assitante for task life')
#result = agent.run_sync('Hello')
#print(result.data)