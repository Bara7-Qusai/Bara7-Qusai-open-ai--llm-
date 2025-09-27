client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""
Transform the following marketing email to use a **professional, positive, and user-centric tone**. 
Keep the message persuasive, highlight the new products, and make the customer feel valued:

{sample_email}
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)
