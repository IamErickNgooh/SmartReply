from dotenv import load_dotenv
from pydantic_ai.agent import Agent

load_dotenv()

agent = Agent(model='groq:gemma2-9b-it', system_prompt='You is powerfull assitante for task life')
result = agent.run_sync('Hello')
print(result.data)

