"""
chain_of_thought_example.py

مثال على استخدام Chain-of-Thought Prompting مع نموذج OpenAI
لحساب عمر والد صديق بعد 10 سنوات مع إظهار خطوات التفكير.
"""

from openai import OpenAI

# تهيئة العميل
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# إنشاء prompt لسلسلة الأفكار
prompt = """
Show your chain-of-thought reasoning step by step before giving the final answer.

Facts:
- My friend is 20 years old.
- His father is currently twice as old as my friend.

Instructions:
1. Write numbered reasoning steps explaining how you calculate the father's current age (show the arithmetic, e.g., 2 × 20 = 40).
2. Then write the steps to calculate the father's age in 10 years (show the arithmetic, e.g., 40 + 10 = 50).
3. After the numbered steps, provide one clear line that starts with "Final Answer:" and gives the father's age in 10 years (include unit "years").

Important: Do not skip the intermediate steps — display each step of your reasoning clearly before the final answer.
"""

# استدعاء النموذج للحصول على الاستجابة
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

# طباعة الاستجابة
print(response.choices[0].message.content)
