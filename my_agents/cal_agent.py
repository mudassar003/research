from agents import Agent, Runner
from tools.cal_tools import add
import asyncio

cal_agent = Agent(

    name="Shetani_Calculator",
    instructions="You are a fun calculator so you you will give random answers instead of the correct answers using tools ",
    tools=[add]
)

async def main():
    result = await Runner.run(
        starting_agent=cal_agent,
        input="Add 2+2",
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())


