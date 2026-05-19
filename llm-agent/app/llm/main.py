# main.py

from langchain.agents import initialize_agent
from langchain.agents import AgentType

from llm.llm import llm
from tools  import action

from llm  import AgentState

state: AgentState = {
    "user_input": "Quanto é 10 + 20?",
    "chat_history": [],
    "intermediate_steps": [],
    "final_response": ""
}


tools = [
    
    action
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.invoke(
    "Quanto é 25 * 40 + 10?"
)

print(response)