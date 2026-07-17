from enum import Enum


class Intent(Enum):

    CHAT = "chat"

    OPEN_APP = "open_app"

    CALCULATOR = "calculator"

    MEMORY = "memory"

    UNKNOWN = "unknown"