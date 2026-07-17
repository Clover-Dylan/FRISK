from config import AI_PROVIDER

from ai.providers.groq_provider import GroqProvider


class ProviderFactory:

    @staticmethod
    def create():

        provider = AI_PROVIDER.lower()

        if provider == "groq":

            return GroqProvider()

        raise ValueError(
            f"Proveedor '{provider}' no soportado."
        )