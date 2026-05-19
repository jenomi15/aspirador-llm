# tools/calculator_tool.py

from langchain.tools import tool

@tool
def action(expression: str) -> str:
    """
    Realiza cálculos matemáticos simples.
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Erro: {str(e)}"