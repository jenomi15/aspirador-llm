# main.py


from langchain.agents import create_agent
from llm.llm import llm
from tools  import action

tools = [
    
    action
]

agent = create_agent(
    system_prompt="""voçê é um agente limpador de salas, seu objetivo é limpar todas as salas possíveis.
                      para isso, voçê tem acesso a uma tool de "action" que pode ser ativada para fazer ações de limpeza.
                     As salas só precisam ser limpas uma vez, nada mais, cada sala tem um nome único.""",
    tools=tools,
    llm=llm,
    
)

response = agent.invoke(
    ""
)

print(response)