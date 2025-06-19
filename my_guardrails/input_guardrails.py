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
    instructions="check if the user input have api key references",
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