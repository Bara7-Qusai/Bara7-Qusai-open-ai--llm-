client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def analyze_portfolio(investments):
    total = sum(investments)
    avg = total / len(investments)
    return avg
"""

# Craft a chain-of-thought prompt using f-string
prompt = f"""
Please analyze the following Python function and explain what it does, step by step.
Function:
{function}

Think carefully about each part of the function, and provide a detailed explanation of its purpose,
inputs, operations, and outputs.
"""

response = get_response(prompt)
print(response)
