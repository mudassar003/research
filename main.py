# main.py
from my_agents.orchestrator_agent import orchestrator_agent
from agents import (
    InputGuardrailTripwireTriggered,
    Runner,
    RunConfig
)
import asyncio
from dotenv import load_dotenv
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()

load_dotenv()

config = RunConfig(
     workflow_name="My custom workflow"
)


async def main():
    """
    Analyze code content provided directly in the code
    """
        # Example: Using direct code content from user input
    user_code_input = """  
            def calculateTotalPrice(items, tax_rate, discount):
                total = 0
                for i in items:
                    total = total + i['price'] * i['quantity']
                if discount > 0:
                    total = total - (total * discount)
                total = total + (total * tax_rate)
                return total

            def process_user_data(user_input):
                # No input validation - security issue
                result = eval(user_input)  # Dangerous!
                return result
    """
    try:   
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input=f"do security analysis of code {user_code_input}",
            run_config=config
    )
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        return f"we cant help"





if __name__ == "__main__":
    asyncio.run(main())