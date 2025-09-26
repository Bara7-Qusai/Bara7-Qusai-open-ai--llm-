client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""
Please summarize the following market research report in **no more than five sentences**, 
focusing specifically on how **AI** and **data privacy** are shaping the market 
and affecting customer behavior:

{report}
"""
response = get_response(prompt)

print("Summarized report: \n", response)
