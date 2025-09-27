client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt =f"""
Step 1: Proofread the following text, correcting any grammar, spelling, or punctuation mistakes 
without changing the original structure or meaning.

Step 2: Adjust the tone of the corrected text to be **formal and friendly**, 
ensuring it remains clear, polished, and engaging for readers.

Text:
{text}
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)
