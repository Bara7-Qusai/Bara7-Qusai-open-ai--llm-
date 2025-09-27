client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = """
Please analyze the following Python function and explain what it does, step by step.
Think carefully about each part of the function, and provide a detailed explanation of its purpose,
inputs, operations, and outputs.
"""
 
response = get_response(prompt)
print(response)
