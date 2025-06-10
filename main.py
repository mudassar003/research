from agents import Agent
from agents import Runner
import asyncio
from dotenv import load_dotenv
import os
from agents import code_analyser

load_dotenv()

async def main():
      result = await Runner.run(code_analyser, "What is the capital of France?")
      print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
