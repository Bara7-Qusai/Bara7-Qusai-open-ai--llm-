client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""
Classify the following customer support ticket into one of three categories: 
1. Technical Issue
2. Billing Inquiry
3. Product Feedback

Respond only with the category name.

Ticket: {ticket}
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)
