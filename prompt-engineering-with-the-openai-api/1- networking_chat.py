from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "You could start with questions like: 'What brings you to this event?', 'Have you attended this event before?', or 'What’s been the most interesting session for you so far?'"}
]

# Create response
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)

print(response.choices[0].message.content)
