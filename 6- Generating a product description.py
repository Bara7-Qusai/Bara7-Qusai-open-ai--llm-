client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Write a persuasive and engaging product description for SonicPro headphones. 
Highlight the following features:
- Active Noise Cancellation (ANC) for immersive sound
- 40-hour battery life for long-lasting use
- Foldable and portable design for convenience
The tone should be professional yet exciting, appealing to music lovers and frequent travelers.

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    temperature=2
)

print(response.choices[0].message.content)
