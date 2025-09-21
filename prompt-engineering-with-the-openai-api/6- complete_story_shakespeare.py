client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a more specific prompt that controls length and style
prompt = f"""Complete the story below in exactly **two paragraphs** and in the style of Shakespeare. 
Delimit the story with triple backticks:

```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\nOriginal story:\n", story)
print("\nGenerated story:\n", response)
