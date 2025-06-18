from agents import function_tool
from typing import List
import re

@function_tool

def check_security(code_content: str) -> str:
    """
    check the security of the code content

    Args:
        code_content: source code content to check for security issues
    Returns:
        A string indicating the security status of the code

    """
    patterns = [
        (r'\beval\s*\(', 'HIGH', 'Use of eval() function'),
        (r'\bexec\s*\(', 'HIGH', 'Use of exec() function'),
        (r'subprocess\.call\s*\([^)]*shell\s*=\s*True', 'HIGH', 'subprocess with shell=True'),
        (r'password\s*=\s*["\'][^"\']+["\']', 'HIGH', 'Hardcoded password'),
        (r'pickle\.loads?\s*\(', 'MEDIUM', 'Use of pickle')
        ]
    
    
    issues : List[str] = []
    lines = code_content.splitlines()

    for i, line in enumerate(lines):
        for pattern, security, description in patterns:
            if re.search(pattern, line):
                issues.append(f"Line {i+1} - {security} - {description}")

    return "\n" .join(issues) if issues else "No security issues found."
