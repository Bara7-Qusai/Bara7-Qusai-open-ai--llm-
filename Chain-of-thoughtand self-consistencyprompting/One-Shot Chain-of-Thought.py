client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
# Define the example
example = "Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.\nA: Even numbers: 10, 4, 2. Adding them: 10 + 4 + 2 = 16."

# Define the question
question = "Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}.\nA:"

# Create the final prompt by combining example and question
prompt = example + "\n\n" + question

# Get the response
response = get_response(prompt)

# Print the response
print(response)
