import secrets
from itertools import chain
from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter

load_dotenv()

class SmartReply:
    store: dict[str, list[bytes]] = {}
    agent: Agent = None
    _session_id: str = 0

    def __init__(self, model: str, prompt: str):
        self._create_session()
        self.agent = Agent(model=model, system_prompt=prompt)
        self.agent.run_sync('he')

    def _create_session(self) -> None:
        self._session_id: str = secrets.token_hex(16)
        self.store[self._session_id]: list[ModelMessage] = [] # type: ignore
     
    def _get_session(self) -> None:
        return self._session_id
    
    def ask_user(self, user_message: str) -> str:
        chat_history = self.get_history()
        response = self.agent.run_sync(user_message, message_history=chat_history)
        self.store_message_in_history(response)
        return response.data
    
    def store_message_in_history(self, result: AgentRunResult[ModelMessage]) -> None:
        session_id = self._get_session()
        self.store[session_id].append(result.new_messages_json())
    
    
    def get_history(self) -> list[ModelMessage]:
        return list(
            chain.from_iterable(
                ModelMessagesTypeAdapter.validate_json(msg_group)
            for msg_group in self.store[self._get_session()]
        )
    )


ask = SmartReply('groq:gemma2-9b-it', 'You is powerfull assitante for task life')
ask._get_session()
print(ask.ask_user('hello'))
print(ask.ask_user('my name is erick '))
print(ask.ask_user('What my name ? '))
