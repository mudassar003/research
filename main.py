# main.py
from my_agents.orchestrator_agent import orchestrator_agent
from agents import (
    InputGuardrailTripwireTriggered,
    Runner,
)
import asyncio
from dotenv import load_dotenv

load_dotenv()


async def main():
    """
    Analyze code content provided directly in the code
    """
    try:
        # Example: Using direct code content from user input
        user_code_input = '''
                        api_key=sk-1234567890abcdef
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
        '''
        
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input=f"Analyze this code content: {user_code_input}",
        )
        
        print(f"Total number of issues found: {result.final_output.issues_found}")
        print(f"Risk level of issue number {result.final_output.issue_number} is {result.final_output.risk_level}")
        print(f"Details of each issue: {result.final_output.summary}")

    except InputGuardrailTripwireTriggered as e:
        print("Due to security issues API keys are not allowed in prompt")


if __name__ == "__main__":
    asyncio.run(main())