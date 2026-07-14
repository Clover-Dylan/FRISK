from dataclasses import dataclass

@dataclass(frozen=True)
class AIModels:
    PRIMARY = "groq/compound"
    BACKUP = "llama-3.3-70b-versatile"