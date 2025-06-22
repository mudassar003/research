import chainlit as cl
from my_agents.orchestrator_agent import orchestrator_agent
from agents import InputGuardrailTripwireTriggered, Runner, RunConfig
from dotenv import load_dotenv

load_dotenv()

config = RunConfig(workflow_name="Security Analysis")

@cl.on_chat_start
async def start():
    """Initialize the chat session with instructions"""
    instructions = """
**Security Code Analyzer**

Welcome! I can analyze your Python code for security vulnerabilities.

**How to use:**
1. Paste your Python code directly into the chat
2. I'll analyze it for security issues and vulnerabilities
3. You'll receive a detailed report with risk levels and recommendations

**What I check for:**
- Dangerous functions (eval, exec, etc.)
- Security vulnerabilities
- Hardcoded credentials
- Unsafe subprocess calls
- Other common security issues

**Risk Levels:**
- HIGH: Critical security vulnerabilities that need immediate attention
- MEDIUM: Important security concerns that should be addressed
- LOW: Minor issues or best practice recommendations

Simply paste your code below to get started.
    """
    await cl.Message(content=instructions).send()

@cl.on_message
async def main(message: cl.Message):
    try:
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input=f"Analyze this code: {message.content}",
            run_config=config
        )
        
        response = f"Issues: {result.final_output.issues_found}\n"
        response += f"Risk: {result.final_output.risk_level}\n"
        response += f"Details: {result.final_output.summary}"
        
        await cl.Message(content=response).send()
        
    except InputGuardrailTripwireTriggered:
        await cl.Message(content="API keys detected and blocked").send()
    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

if __name__ == "__main__":
    cl.run()