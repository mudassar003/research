from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)
class ApiKeyCheckOutput(BaseModel):
    contains_api_key: bool
    reasoning: str

api_key_guardrail_agent = Agent(
    name="Api key guardrail",
    instructions="""
                You are checking for API keys or secrets in code/text.
                
                Look for these common patterns:
                1. Strings starting with 'sk-' (OpenAI keys)
                2. Variables named api_key, secret, token with values
                3. Environment variables like OPENAI_API_KEY with values
                4. Any obvious credential assignments
                
                Examples that should trigger:
                - api_key = "sk-1234567890"
                - SECRET_KEY = "mysecret" 
                - OPENAI_API_KEY: "value"
                - api_key = 123456sk
                
                Return contains_api_key=True if you find ANY of these patterns.
                Be conservative - if in doubt, flag it as containing an API key.
    """,
    output_type=ApiKeyCheckOutput
)

@input_guardrail
async def input_guardrail_agent(
    ctx: RunContextWrapper, agent:Agent, input:str
) -> GuardrailFunctionOutput:
    """
    input guardrail to check api reference in user input
    """

    result = await Runner.run(api_key_guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_api_key,
    )