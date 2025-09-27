client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = (
    "You are a friendly and knowledgeable learning advisor chatbot. "
    "Your role is to ask learners about their background, prior experience, and learning goals, "
    "then recommend a personalized path of textbooks. "
    "Always include beginner-level books to help them start and advanced books to help them progress further. "
    "Explain briefly why each book is useful for their journey."
)
user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)
