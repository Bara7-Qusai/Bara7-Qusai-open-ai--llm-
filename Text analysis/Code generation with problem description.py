client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = """
Write a Python function named `highest_sales_month` that takes a list of 12 numbers representing monthly sales,
and returns the name of the month (January, February, …) with the highest sales.
"""

response = get_response(prompt)
print(response)
