client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Classify the following text into an emotion category. 
Possible emotions: Happiness, Sadness, Fear, Surprise, Anger, Disgust, or 'no explicit emotion' if there is none.

Examples:
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
They sat and ate their meal -> no explicit emotion
Time flies like an arrow -> no explicit emotion

Now classify the following:
"I forgot to lock the door last night" ->
"""


response = get_response(prompt)
print(response)
