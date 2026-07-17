from __future__ import annotations


class PromptManager:
    """
    Administra el mensaje del sistema que se envía
    antes de cada conversación.
    """

    def __init__(self):

        self._system_prompt = """
Eres FRISK, un asistente personal de escritorio.

Reglas:

- Responde en español por defecto.
- Sé claro y preciso.
- Si el usuario pide código, genera código limpio.
- Si no sabes algo, dilo claramente.
- No inventes información.
- Mantén un tono amable y profesional.
""".strip()

    def get_system_message(self) -> dict[str, str]:

        return {
            "role": "system",
            "content": self._system_prompt
        }

    def set_prompt(self, prompt: str) -> None:

        self._system_prompt = prompt

    def get_prompt(self) -> str:

        return self._system_prompt