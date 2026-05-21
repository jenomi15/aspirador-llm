# tools.py
from langchain.tools import tool
# CORREÇÃO: Importação direta do arquivo environment.py local
from app.environment import environment

@tool
def action() -> str:
    """
    Limpa uma sala.
    """
    return environment.limpar_quarto()

@tool
def see() -> str:
    """
    Vê o estado atual da sala.
    """
    return environment.ver_quarto_atual()

@tool
def move(direcao: str) -> str:
    """
    Move o robô para outra sala (recebe 'MOVELEFT' ou 'MOVERIGHT').
    """
    return environment.mover(direcao)

@tool
def finished() -> str:
    """
    Verifica se todas as salas estão limpas.
    """
    # CORREÇÃO: Adicionado o retorno que faltava
    return str(environment.terminou())