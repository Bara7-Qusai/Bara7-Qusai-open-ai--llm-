client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "If a customer asks about an order but does not provide an order number, politely ask them to provide the order number before proceeding. "

# Define the technical issue condition
technical_issue_condition = "If a customer reports a technical issue, start your response with 'I'm sorry to hear about your issue with ...' and then provide helpful troubleshooting steps. "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)
