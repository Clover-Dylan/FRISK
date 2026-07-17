from __future__ import annotations

from config import MAX_HISTORY


class ConversationManager:
    """
    Administra el historial de conversación de FRISK.
    """

    def __init__(self):

        self._messages: list[dict[str, str]] = []

    def add_user(self, text: str) -> None:

        self._messages.append({
            "role": "user",
            "content": text
        })

        self._trim()

    def add_assistant(self, text: str) -> None:

        self._messages.append({
            "role": "assistant",
            "content": text
        })

        self._trim()

    def get_messages(self) -> list[dict[str, str]]:

        return self._messages.copy()

    def clear(self) -> None:

        self._messages.clear()

    def message_count(self) -> int:

        return len(self._messages)

    def _trim(self) -> None:
        """
        Mantiene solo los últimos MAX_HISTORY mensajes.
        """

        if len(self._messages) > MAX_HISTORY:

            self._messages = self._messages[-MAX_HISTORY:]