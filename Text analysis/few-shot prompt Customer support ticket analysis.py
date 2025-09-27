client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = """
Extract the key entities from customer support tickets. 
Use the examples below to understand how to extract entities and display them.

Example 1:
Ticket: {ticket_1}
Entities: {entities_1}

Example 2:
Ticket: {ticket_2}
Entities: {entities_2}

Example 3:
Ticket: {ticket_3}
Entities: {entities_3}

Now, extract the entities from the following ticket:
Ticket: {ticket_4}
Entities:
"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)
