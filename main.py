from my_agents.orchestrator_agent import orchestrator_agent
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel, Field
# from agents.extensions.visualization import draw_graph

load_dotenv()



async def main():
    try:
        file_path = "sample.py"
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input="Use the orchestrator agent and analyze sample.py.File path for read_source_file tool is 'sample.py'",
        )
        print (f" Total number of issues found: {result.final_output.issues_found}")
        print (f"Risk level of issue number  {result.final_output.issue_number} is {result.final_output.risk_level} ")
        print (f"Details of each issue {result.final_output.summary}")

    except InputGuardrailTripwireTriggered as e:
        print("Due to security issues API keys are not allowed in prompt")

if __name__ == "__main__":
    asyncio.run(main())