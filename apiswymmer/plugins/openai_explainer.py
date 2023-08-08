import openai
from dotenv import load_dotenv
import os
from typing import Any

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_code_explanation(code_str: Any) -> str:
    """Gives a code explanation using the OpenAI API."""
    response = openai.ChatCompletion.create(
        engine="davinci-codex",
        prompt=f'"""\nPython code explanation\n"""\n\n"""\n{code_str}\n"""\n\n"""\nExplanation:\n"""\n',
        temperature=0.3,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['"""'],
    )
    return response.choices[0].text
