from agents import Agent
from my_agents.security_agent import security_agent
from tools.file_tools import read_source_file

orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions="You are an orchestrator agent. You will use tool read_source_file to read the source code file " \
    "and then you will use tool security_agent to analyze the security of the code. " \
    "You will explain each issue found in one line or sentence.",
    tools=[read_source_file,
           security_agent.as_tool(
               tool_name="Security Agent",
               tool_description="Do security analysis of the code and explain each issue found in one line or sentence."),
           ]
)