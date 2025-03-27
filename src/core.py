from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.messages import ModelMessage
from pydantic_ai.agent import AgentRunResult


load_dotenv()

def create_agent(model: str, prompt: str) -> Agent: 
    agent: Agent = Agent(model=model, system_prompt=prompt)
    return agent

store: dict[str, list[bytes]] = {}

def create_session_if_not_exists(session_id: str) -> None:
    if session_id not in store:
        store[session_id]: list[ModelMessage] = [] # type: ignore

def store_messages_in_history(session_id: str, message: AgentRunResult[ModelMessage]) -> None:
    create_session_if_not_exists(session_id)
    store[session_id].append(message.new_messages_json())
 
agent = create_agent('groq:gemma2-9b-it', 'You is powerfull assitante for task life')
result = agent.run_sync('Hello')
store_messages_in_history('user123', result)

for _, value in store.items():
    print("test _____ ", value)