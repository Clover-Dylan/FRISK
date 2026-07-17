from dataclasses import dataclass


@dataclass(slots=True)
class StreamChunk:
    content: str
    finished: bool = False