from openai import OpenAI

client = OpenAI(api_key = 'open_api_key'

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(completion.choices[0].message)
print(completion.choices[0].message)
print(completion.choices[0].message)

def square(num):
  return num ** 2
print(square(2))