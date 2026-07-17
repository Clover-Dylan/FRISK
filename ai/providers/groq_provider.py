from groq import Groq

from config import (
    GROQ_API_KEY,
    PRIMARY_MODEL
)

from ai.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

        self.model = PRIMARY_MODEL

    def name(self) -> str:

        return "Groq"

    def chat(self, messages: list[dict]) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages=messages

        )

        return response.choices[0].message.content