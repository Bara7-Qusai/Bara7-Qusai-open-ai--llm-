client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f"""
Translate the following English marketing message into **French, Spanish, and Japanese**. 
Keep the tone professional and suitable for introducing a premium product:

{marketing_message}
"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)
