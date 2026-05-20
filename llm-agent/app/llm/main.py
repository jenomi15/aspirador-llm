# main.py
from typing_extensions import TypedDict
from langchain.agents import create_agent
from llm.llm import llm
from tools.tools import see, move, action,finished

tools = [
    see,
    move,
    action,
    finished
]

agent = create_agent(
    system_prompt="""Você é um robô aspirador autônomo em uma casa linear com duas salas."
                "SUA VISÃO É LIMITADA: Você só pode ver a sala onde está parado no momento."
                "Seu objetivo é garantir que AMBAS as salas estejam limpas."
                "Estratégia sugerida:"
                "1. Use 'see' para ver a sala atual."
                "2. Se estiver suja, use 'action'."
                "3. Use 'move' (MOVELEFT ou MOVERIGHT) para ir para a outra sala e repetir o processo."
                "4. finished é usado para voc parar
                "Certifique-se de verificar ambas as salas antes de concluir a tarefa.""",
    tools=tools,
    llm=llm,
    
)

response = agent.invoke(
    {"input": "comece a limpeza"}
)

print(response)