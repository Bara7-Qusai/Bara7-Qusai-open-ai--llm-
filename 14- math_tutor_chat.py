from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,  # <-- fill in the messages list
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {
    "role": "assistant",  # <-- role of the AI
    "content": response.choices[0].message.content  # <-- content from the model
}

# Add assistant_dict to the messages list
messages.append(assistant_dict)  # <-- append to keep conversation history

# Print the full conversation
print(messages)
