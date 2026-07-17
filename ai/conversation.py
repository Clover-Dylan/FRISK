from __future__ import annotations


class Conversation:
    """
    Historial temporal de conversación.
    """

    def __init__(self):

        self.messages = []

    def add_user(self, text: str):

        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )

    def add_assistant(self, text: str):

        self.messages.append(
            {
                "role": "assistant",
                "content": text
            }
        )

    def clear(self):

        self.messages.clear()

    def history(self):

        return self.messages.copy()