client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""
Please expand the following smart home security camera product description into a **comprehensive one-paragraph overview**. 
The expanded description should clearly highlight the product's **unique features, benefits, and potential applications**, 
while making it informative and engaging for potential customers:

{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)
