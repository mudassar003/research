import chainlit as cl
from my_agents.orchestrator_agent import orchestrator_agent
from agents import Runner
from dotenv import load_dotenv

load_dotenv()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="🤖 Ready to test your orchestrator agent!"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    try:
        # Run the orchestrator agent with user input
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input=message.content,
        )
        
        # Send results
        await cl.Message(content=result.final_output).send()
        
    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

if __name__ == "__main__":
    cl.run()