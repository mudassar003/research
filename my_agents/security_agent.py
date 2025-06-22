from agents import Agent
from my_tools.security_tools import check_security

security_agent = Agent(
    name="Security Analyser",
    instructions="""
    use your tool get all info from it and summarise it in minimum number of lines
    """,
    tools=[check_security],
    
)