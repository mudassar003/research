from agents import Agent
from tools import file_tools

code_analyser = Agent(
    name="Code Analyser",
    instructions=""" You are a code analysis expert. Analysis python file for:
      - Code complexity issues
      - Code smells antipatterns
      - Fuction length and complexity
      - Documentation quality  """
      tools=[file_tools]
)
