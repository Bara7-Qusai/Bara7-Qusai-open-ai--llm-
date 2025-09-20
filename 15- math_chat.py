# Import the OpenAI client and set up your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Initialize a conversation with a system message defining the assistant's behavior
messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]

# List of user questions/messages
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over each user question
for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the current user message
    # Note: 'role' should be a string "user", not a variable
    user_dict = {"role": "user", "content": q}
    
    # Append the user message to the conversation history
    messages.append(user_dict)
    
    # Make a chat completion request to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Choose the model
        messages=messages,    # Provide the full conversation history
        max_completion_tokens=100  # Limit the response length
    )
    
    # Extract the assistant's reply from the response
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    
    # Append the assistant's message to the conversation history
    messages.append(assistant_dict)
    
    # Print the assistant's response
    print("Assistant: ", response.choices[0].message.content, "\n")
