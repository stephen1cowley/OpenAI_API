import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts


# load the .env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPEN_AI_API_KEY')
)


model = "gpt-3.5-turbo"
temperature = 0.7
max_tokens = 500

system_message = prompts.system_message
user_message = prompts.first_message

messages =[
    {"role": "system", "content":system_message},
    {"role": "user", "content":user_message}
]

def get_response():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content

print(get_response())
