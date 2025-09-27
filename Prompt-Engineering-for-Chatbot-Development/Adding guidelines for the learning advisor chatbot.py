client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = (
    "Act as a learning advisor who receives queries from users mentioning their background, "
    "experience, and goals, and accordingly provides a response that recommends a tailored "
    "learning path of textbooks, including both beginner-level and more advanced options."
)

# Define behavior guidelines
behavior_guidelines = (
    " If the user does not provide information about their background, experience, "
    "and goals, politely ask them to share these details before giving recommendations. "
    " Always keep a friendly and encouraging tone."
)

# Define response guidelines
response_guidelines = (
    " Provide recommendations in a clear structure with two sections: beginner-level and advanced-level textbooks. "
    " Include no more than 3 textbooks in each section, and mention the author names. "
    " For each textbook, add a short explanation of why it is useful for the learner’s goals."
)

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines

user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"

response = get_response(system_prompt, user_prompt)
print(response)

