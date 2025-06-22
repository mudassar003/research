from agents import Agent
from my_agents.security_agent import security_agent
from my_tools.code_processor import analyze_code_content
from my_guardrails.input_guardrails import input_guardrail_agent
from pydantic import BaseModel, Field


class SecurityAnalysisOutput(BaseModel):
    issues_found:str = Field(description = "total number of issues of found in file")
    risk_level:str = Field(description = "level of each issue eaither low, mid or high")
    summary:str = Field(description = "one line description of each issue")
    issue_number:str = Field(description = "index number of issue")


orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions=""" You are an orchestrator agent. You will use tool read_source_file to read the source code file 

    Use analyse_code_content to process code from user input, then use security_agent to analyze 
    the security of code. You will explain eache issue in one line or sentence.

    The user will provide content directly to their input so you will extract and analyse it.
    """ 
    ,
    tools=[analyze_code_content,
           security_agent.as_tool(
               tool_name="Security_Agent",
               tool_description="Do security analysis of the code and explain each issue found in one line or sentence."),
           ],
    input_guardrails=[input_guardrail_agent],
    output_type=SecurityAnalysisOutput
)
