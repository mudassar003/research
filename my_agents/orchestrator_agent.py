from agents import Agent
from my_agents.security_agent import security_agent
from my_guardrails.input_guardrails import input_guardrail_agent

orchestrator_agent = Agent(
    name="Security Code Orchestrator",
    instructions="""
        send code to suitble agent based on user prompt for security or quality analysis
    """,
    handoffs=[security_agent],
    input_guardrails=[input_guardrail_agent],

)