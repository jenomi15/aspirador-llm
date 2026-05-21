from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from app.tools import see, move, action, finished

from dotenv import load_dotenv
import os

load_dotenv()

tools = [
    see,
    move,
    action,
    finished
]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

agent = create_agent(
    system_prompt=(
        "Você é um robô aspirador autônomo em uma casa linear com duas salas.\n"
        "SUA VISÃO É LIMITADA: Você só pode ver a sala onde está parado no momento.\n"
        "Seu objetivo é garantir que AMBAS as salas estejam limpas.\n"
        "Estratégia sugerida:\n"
        "1. Use 'see' para ver a sala atual.\n"
        "2. Se estiver suja, use 'action'.\n"
        "3. Use 'move' (MOVELEFT ou MOVERIGHT) para ir para a outra sala e repetir o processo.\n"
        "4. finished é usado para você parar.\n"
        "Certifique-se de verificar ambas as salas antes de concluir a tarefa."
    ),
    tools=tools,
    model=llm,
)

response = agent.invoke(
    {
        "messages": [
            ("user", "comece a limpeza")
        ]
    }
)

for message in response["messages"]:
    message.pretty_print()