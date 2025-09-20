client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisbon, and it is known for its Atlantic coastline, maritime history, and vibrant culture."},

        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)
