# my_agents/orchestrator_agent.py
from agents import Agent
from my_agents.security_agent import security_agent
from my_guardrails.input_guardrails import input_guardrail_agent

orchestrator_agent = Agent(
    name="Security Code Orchestrator",
    instructions="""
    You are a code analysis orchestrator. Your role is to:
    
    1. Analyze the user's request to determine what type of analysis is needed
    2. If the request involves code security analysis, transfer to the Security Analyser
    3. Only make ONE handoff per request - do not make multiple handoffs
    4. Be decisive - once you identify the need for security analysis, immediately transfer
    
    Guidelines:
    - For security-related requests: transfer to Security Analyser
    - For code quality requests: transfer to Security Analyser (it can handle both)
    - Make only ONE transfer call per response
    - Do not analyze the code yourself - delegate to the appropriate specialist
    """,
    handoffs=[security_agent],
    input_guardrails=[input_guardrail_agent]
)

