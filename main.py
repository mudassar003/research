from my_agents.orchestrator_agent import orchestrator_agent
from agents import Runner
import asyncio
from dotenv import load_dotenv
from agents.extensions.visualization import draw_graph

load_dotenv()

async def main():
    file_path = "sample.py"
    result = await Runner.run(
        starting_agent=orchestrator_agent,
        input="Use the orchestrator agent and give me output that you get from it. File path for read_source_file tool is 'sample.py'.",
    )
    print(result.final_output)

    draw_graph(orchestrator_agent, filename="my_workflow.png")

if __name__ == "__main__":
    asyncio.run(main())
