def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


functions = [
    {
        "name": "add",
        "description": "Add two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "subtract",
        "description": "Subtract two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "divide",
        "description": "Divide two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    }
]


import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
import requests

GPT_MODEL = "gpt-3.5-turbo"
openai.api_key = 'open_api_key'

@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, functions=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

class Conversation:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        for message in self.conversation_history:
            print(
                colored(
                    f"{message['role']}: {message['content']}\n\n",
                    role_to_color[message["role"]],
                )
            )
import re

def apply_operator(operator, a, b):
    if operator == 'plus':
        return add(a, b)
    elif operator == 'minus':
        return subtract(a, b)
    elif operator == 'into':
        return multiply(a, b)
    elif operator == 'divide':
        return divide(a, b)

def precedence(op):
    if op in ['plus', 'minus']:
        return 1
    if op in ['into', 'divide']:
        return 2
    return 0

def infix_to_postfix(expression):
    tokens = re.findall(r'\d+|plus|minus|into|divide', expression)
    stack = []
    output = []

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isnumeric():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(token, a, b)
            stack.append(result)

    return stack[0]

def process_query(query):
    postfix_expression = infix_to_postfix(query)
    result = evaluate_postfix(postfix_expression)
    return result
# Create a conversation
conversation = Conversation()

# Add user query
user_query = "34 plus 45 divide by 3 into 5 = "
conversation.add_message("user", user_query)

# Process the user query
result = process_query(user_query)
print(f"Result of '{user_query}': {result}")



# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b



# functions = [
#     {
#         "name": "add",
#         "description": "Add two numbers",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number", "description": "The first number"},
#                 "b": {"type": "number", "description": "The second number"}
#             },
#             "required": ["a", "b"]
#         }
#     },
#     {
#         "name": "subtract",
#         "description": "Subtract two numbers",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number", "description": "The first number"},
#                 "b": {"type": "number", "description": "The second number"}
#             },
#             "required": ["a", "b"]
#         }
#     },
#     {
#         "name": "multiply",
#         "description": "Multiply two numbers",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number", "description": "The first number"},
#                 "b": {"type": "number", "description": "The second number"}
#             },
#             "required": ["a", "b"]
#         }
#     },
#     {
#         "name": "divide",
#         "description": "Divide two numbers",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number", "description": "The first number"},
#                 "b": {"type": "number", "description": "The second number"}
#             },
#             "required": ["a", "b"]
#         }
#     }
# ]


# import openai
# from tenacity import retry, wait_random_exponential, stop_after_attempt
# import requests

# GPT_MODEL = "gpt-3.5-turbo"
# openai.api_key = 'OPENAI_API_KEY'  # Replace with your OpenAI API key

# @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
# def chat_completion_request(messages, functions=None, model=GPT_MODEL):
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer " + openai.api_key,
#     }
#     json_data = {"model": model, "messages": messages}
#     if functions is not None:
#         json_data.update({"functions": functions})
#     try:
#         response = requests.post(
#             "https://api.openai.com/v1/chat/completions",
#             headers=headers,
#             json=json_data,
#         )
#         return response
#     except Exception as e:
#         print("Unable to generate ChatCompletion response")
#         print(f"Exception: {e}")
#         return e


# def process_query(query):
#     conversation = [
#         {"role": "user", "content": query}
#     ]
#     response = chat_completion_request(
#         conversation,
#         functions=functions
#     )
#     response_data = response.json()
#     if 'choices' in response_data and len(response_data['choices']) > 0:
#         return response_data['choices'][0]['message']['content']
#     else:
#         return "Error processing the query."

# def main():
#     while True:
#         # Get user input for arithmetic expression
#         user_query = input("Enter your arithmetic expression (or type 'exit' to quit): ")
#         if user_query.lower() == 'exit':
#             break
        
#         # Process the query using OpenAI API
#         result = process_query(user_query)
#         print(f"Result: {result}")

# if __name__ == "__main__":
#     main()

