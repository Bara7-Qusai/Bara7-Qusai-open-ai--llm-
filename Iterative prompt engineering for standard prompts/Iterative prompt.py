client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Provide a table of the top 10 pre-trained language models. 
The table should include three columns: 
1. Model Name
2. Release Year
3. Owning Company
Please format it clearly as a markdown table.
"""

response = get_response(prompt)
print(response)
