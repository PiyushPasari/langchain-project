import json
from tools import search_web, calculator

TOOL_MAP = {
    "search_web": search_web,
    "calculator": calculator
}

def run_agent(messages, llm, tool_schemas):

    while True:

        response = llm(messages, tools=tool_schemas)
        msg = response.choices[0].message

        if msg.tool_calls:
            for tool_call in msg.tool_calls:

                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                result = TOOL_MAP[name](**args)

                messages.append({
                    "role": "tool",
                    "content": result,
                    "tool_call_id": tool_call.id
                })

        else:
            return msg.content