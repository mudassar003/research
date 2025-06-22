from agents import function_tool 

@function_tool

def analyze_code_content(code_content: str) -> str:
    """
    Analyse code directly from user input

    Args:
        code_content: The source code content to analyse

    Return:
        The code content formatted for analysis

    """

    try:
        if not code_content or not code_content.strip():
            return "No code content provided"
        
        if len(code_content.strip()) < 10 :
            return "The provided content appears to be too short"
        
        return f"Code Content Analysis \n\n Content: \n\n {code_content}"
    
    except Exception as e:
        f"Error analyzing code content: {str(e)}"

