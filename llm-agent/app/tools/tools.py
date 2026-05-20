# tools/calculator_tool.py

from langchain.tools import tool

@tool
def action(expression: str) -> str:
    """
    Limpa uma sala.
    """

