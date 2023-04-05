import openai
from llm_chat.config import API_KEY

def prompt_completion(context, prompt, model="text-davinci-003", max_tokens=1000):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()
