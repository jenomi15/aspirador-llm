# tools/calculator_tool.py
from langchain.tools import tool
from environment.environment import environment
@tool
def action(expression: str) -> str:
    """
    Limpa uma sala.
    """
    return environment.limpar_quarto()
@tool
def see(expression: str) -> str:
    """
    Vê o estado atual da sala.
    """
    return environment.ver_quarto_atual()
@tool
def move(direcao: str) -> str:
    """
    Vê o estado atual da sala.
    """
    return environment.mover(direcao)

@tool
def finished(_: str) -> str:
    """
    Verifica se todas as salas estão limpas.
    """
    return str(environment.terminou())