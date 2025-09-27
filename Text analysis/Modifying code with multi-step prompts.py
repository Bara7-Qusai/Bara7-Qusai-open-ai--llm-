client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
You are given the following Python function:

{function}

Please modify this function in the following way:
1. Check if both `width` and `length` are positive numbers. If not, return an appropriate error message.
2. If the inputs are valid, calculate both the area and the perimeter of the rectangle.
3. Return both the area and perimeter as a tuple.

Make sure the modified function is complete and ready to use.
"""

response = get_response(prompt)
print(response)
