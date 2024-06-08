from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get('OPEN_AI_API_KEY')
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Recite 10 digits of pi to me, backwards."
        }],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
