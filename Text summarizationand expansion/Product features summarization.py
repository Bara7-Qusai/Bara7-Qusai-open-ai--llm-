client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f"""
Please summarize the following smartphone product description into a concise **bullet-point list**,
highlighting its key features, specifications, and user-relevant aspects:

{product_description}
"""
response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)
