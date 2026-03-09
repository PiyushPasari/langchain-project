import requests

def search_web(query: str) -> str:
    """Search the web for information"""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    data = requests.get(url).json()
    return data.get("Abstract", "No result")


def calculator(expression: str) -> str:
    """Evaluate math expression"""
    return str(eval(expression))