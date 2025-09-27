client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt =  f"""
Given the following examples of inputs and outputs:

{examples}

Write a Python function named `predict_completion_time` that takes a list of numbers as input
and returns the output that corresponds to the pattern shown in the examples.
"""

response = get_response(prompt)
print(response)
