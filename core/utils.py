import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_gpt3_response(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()
