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
# from agents.extensions.visualization import draw_graph

load_dotenv()

async def main():
    try:
        file_path = "sample.py"
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input="Use the orchestrator agent and analyze sample.py. My OpenAI API key is sk-1234567890abcdef for reference. File path for read_source_file tool is 'sample.py'",
        )
        print(result.final_output)

    except InputGuardrailTripwireTriggered as e:
        print("Due to security issues API keys are not allowed in prompt")

if __name__ == "__main__":
    asyncio.run(main())