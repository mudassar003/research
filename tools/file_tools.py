import os
from agents import function_tool


@function_tool
def read_source_file(file_path: str) -> str:
    """
    Read contents of the source code file

    Args:
        file_path: path to the source file to read

    Returns:
        The file contents as a string
    """

    try:
        if not os.path.exists(file_path):
            return f"File {file_path} does not exist."
        
        if not file_path.endswith(".py"):
            return f"File {file_path} is not supported"
        
        with open(file_path, 'r', encoding="utf-8") as f:
            content=f.read()

        return f"File: {file_path} \n\n Content: \n\n {content}"
    
    except Exception as e:
        return f"error loading file : {str(e)}"

