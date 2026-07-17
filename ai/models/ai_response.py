from dataclasses import dataclass


@dataclass(slots=True)
class AIResponse:

    content: str

    provider: str

    model: str

    latency: float