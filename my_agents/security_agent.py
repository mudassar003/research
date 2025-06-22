# my_agents/security_agent.py
from agents import Agent
from my_tools.security_tools import check_security

security_agent = Agent(
    name="Security Analyser",
    instructions="""
    You are a security analysis specialist. Your responsibilities:
    
    1. Use the check_security tool to analyze the provided code
    2. Interpret the security findings 
    3. Provide summarized findings for each error in one line

    Always use your security tool first before providing analysis.
    """,
    tools=[check_security],
)