from __future__ import annotations

from core.application import Application


class Assistant:
    """
    Punto de entrada para interactuar con FRISK.

    Coordina los distintos módulos de la aplicación,
    pero no implementa su lógica interna.
    """

    def __init__(self, app: Application):

        self.app = app

        self.logger = app.get("logger")

        self.events = app.get("events")

    def start(self):

        self.logger.info("Assistant iniciado.")

        self.app.start()

    def stop(self):

        self.logger.info("Assistant detenido.")

        self.app.stop()

    def process_message(self, message: str) -> str:
        """
        Procesa un mensaje del usuario.

        En los próximos sprints este método utilizará:
        - Router
        - Plugins
        - IA
        - Memoria
        """

        self.logger.info(f"Usuario: {message}")

        self.events.emit("user_message", message)

        return f"Has dicho: {message}"