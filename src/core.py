from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter
from pydantic_ai.agent import AgentRunResult
from itertools import chain


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

def get_chat_history(session_id: str) -> list[ModelMessage]:
    create_session_if_not_exists(session_id)
    return list(chain.from_iterable(
        ModelMessagesTypeAdapter.validate_json(msg_group)
        for msg_group in store[session_id]
    ))
 
 
agent = create_agent('groq:gemma2-9b-it', 'You is powerfull assitante for task life')
result = agent.run_sync('Hello')
store_messages_in_history('user123', result)
result = agent.run_sync('What is hello world')
store_messages_in_history('user123', result)
print(get_chat_history('user123'))
