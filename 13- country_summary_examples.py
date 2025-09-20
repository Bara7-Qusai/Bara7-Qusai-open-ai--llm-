client = OpenAI(api_key="<OPENAI_API_TOKEN>")
example1 = {"role": "user", "content": "Give me a quick summary of Japan."}
response1 = {"role": "assistant", "content": "Japan is an island country in East Asia, located in the Pacific Ocean. Its capital city is Tokyo."}

example2 = {"role": "user", "content": "Give me a quick summary of Brazil."}
response2 = {"role": "assistant", "content": "Brazil is the largest country in South America. Its capital is Brasília, and it is famous for the Amazon rainforest."}

example3 = {"role": "user", "content": "Give me a quick summary of Canada."}
response3 = {"role": "assistant", "content": "Canada is a country in North America known for its vast landscapes and cold climate. Its capital city is Ottawa."}
 
response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   
   messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        example1,
        response1,
        example2,
        response2,
        example3,
        response3,
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)
