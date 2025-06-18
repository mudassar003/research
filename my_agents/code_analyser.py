from agents import Agent
from my_tools.file_tools import read_source_file  # import the actual decorated function

code_analyser = Agent(
    name="Code analyser agent",
    instructions=(
        "You will use the read_source_file tool to read the file. "
        "If the tool response includes an error (e.g., starts with 'File' or 'error'), "
        "you should return that as your final output without trying to analyze the code. "
        "Otherwise, give a one-line code quality review."
    ),
    tools=[read_source_file]
)