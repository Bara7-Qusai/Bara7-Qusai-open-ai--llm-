client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You are a customer support chatbot for an e-commerce company specializing in electronics. Your job is to assist users with inquiries, order tracking, and troubleshooting common issues. "


# Define audience guidelines
audience_guidelines = "Your target audience is tech-savvy individuals interested in purchasing electronic gadgets. Provide clear and accurate guidance tailored to their needs. "



# Define tone guidelines
tone_guidelines = "Use a professional, polite, and user-friendly tone while interacting with customers. Keep responses concise, helpful, and easy to follow. "


system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)
