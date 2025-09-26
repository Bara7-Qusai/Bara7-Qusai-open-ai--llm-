client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction ="""
Solve the following problem by imagining that 3 independent experts each try to solve it. 
Each expert should reason step by step and give their answer. 
Finally, determine the final answer by majority vote among the 3 experts.
"""

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + "\n\nProblem:\n" + problem_to_solve


response = get_response(prompt)
print(response)
