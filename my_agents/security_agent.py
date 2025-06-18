from agents import Agent
from my_tools.security_tools import check_security

security_agent = Agent(
    name="Security Analyser",
    instructions="You are a security expert. You will use tool check_security to analyze the security " \
    "and then will explain each issue found  in one line or sentencce.",
    tools=[check_security]
)