import time

from ai.models.ai_response import AIResponse
from ai.providers import ProviderFactory


class AIEngine:

    def __init__(self, provider=None):

        self.provider = provider or ProviderFactory.create()

    def chat(self, messages):

        start = time.perf_counter()

        answer = self.provider.chat(messages)

        latency = time.perf_counter() - start

        return AIResponse(
            content=answer,
            provider=self.provider.name(),
            model=self.provider.model,
            latency=latency
        )