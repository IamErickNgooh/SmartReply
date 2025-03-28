import secrets
from dotenv import load_dotenv
from pydantic_ai.agent import Agent, AgentRunResult
from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter
import streamlit as st


load_dotenv()

class SmartReply:
    def __init__(self, model: str, prompt: str):
        self.store: dict[str, list[ModelMessage]] = {}
        self.session_id: str = self._create_session()
        self.agent: Agent = Agent(model=model, system_prompt=prompt)

    def _create_session(self) -> str:
        session_id = secrets.token_hex(16)
        self.store[session_id] = []
        return session_id

    def get_session(self) -> str:
        return self.session_id

    def ask_user(self, user_message: str) -> str:
        chat_history = self.get_history()
        response = self.agent.run_sync(user_message, message_history=chat_history)
        self._store_message_in_history(response)
        return response.data

    def _store_message_in_history(self, result: AgentRunResult[ModelMessage]) -> None:
        messages = ModelMessagesTypeAdapter.validate_json(result.new_messages_json())
        self.store[self.session_id].extend(messages)  # <- bien aplati

    def get_history(self) -> list[ModelMessage]:
        return self.store[self.session_id]


st.title('Hello World')
st.write('Ceci est ma première app.')