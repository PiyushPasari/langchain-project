from openai import OpenAI
client = OpenAI()

def call_llm(messages, tools=None):
    response = client.chat.completions.create(
        model=gpt-4o-mini,
        messages=messages,
        tools=tools
    )
    return response
