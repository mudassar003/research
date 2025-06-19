from my_agents.orchestrator_agent import orchestrator_agent
from agents import Runner
import asyncio
from dotenv import load_dotenv
# from agents.extensions.visualization import draw_graph
from my_guardrails.input_guardrails import input_guarail_agent

load_dotenv()

async def main():
    file_path = "sample.py"
    result = await Runner.run(
        starting_agent=orchestrator_agent,
        input="Use the orchestrator agent and give me output that you get from it. File path for read_source_file tool is 'sample.py'.",
        input_guardrails=[input_guardrail_agent],
    )
    print(result.final_output)

    

if __name__ == "__main__":
    asyncio.run(main())
