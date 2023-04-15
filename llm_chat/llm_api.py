import openai
from llm_chat.config import API_KEY, DEFAULT_MODEL, DEFAULT_MAX_TOKENS

def prompt_completion(context, prompt, model=DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS):
    """
    Generate completions based on a given context and prompt using the OpenAI API.

    Parameters:
        context (str): The context for the completion.
        prompt (str): The prompt text based on which the completion will be generated.
        model (str): The language model to be used for generating the completion.
        max_tokens (int): The maximum number of tokens to be generated in the completion.

    Returns:
        str: The generated completion text.
    """
    openai.api_key = API_KEY
    full_prompt = context + prompt

    try:
        response = openai.Completion.create(
            engine=model,
            prompt=full_prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.8,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle exceptions related to the OpenAI API
        return str(e)
