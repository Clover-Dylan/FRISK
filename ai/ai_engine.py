import time

from ai.providers import ProviderFactory
from ai.models.ai_response import AIResponse


class AIEngine:

    def __init__(self):

        self.provider = ProviderFactory.create()

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
    
    def stream_chat(self, messages):

        response = self.provider.chat(messages)

        words = response.split()

        for word in words:

            yield word + " "

        yield ""