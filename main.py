from my_agents.code_analyser import code_analyser
from agents import Runner
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    file_path = "sample.py"
    result = await Runner.run(
        starting_agent=code_analyser,
        input=f"read_source_file file_path='{file_path}' and give review"
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
