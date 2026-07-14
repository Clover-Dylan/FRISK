from __future__ import annotations

from core.logger import Logger
from core.service_container import ServiceContainer
from core.event_bus import EventBus


class Application:
    """
    Núcleo principal de FRISK.

    Se encarga de crear todos los servicios
    compartidos y registrarlos en el contenedor.
    """

    def __init__(self):

        self.container = ServiceContainer()

        self.logger = Logger()

        self.events = EventBus()

        self._register_services()

        self.logger.info("Application creada.")

    def _register_services(self):

        self.container.register("logger", self.logger)

        self.container.register("events", self.events)

        self.container.register("application", self)

    def get(self, service: str):

        return self.container.get(service)

    def start(self):

        self.logger.info("FRISK iniciado.")

        self.events.emit("app_started")

    def stop(self):

        self.logger.info("FRISK detenido.")

        self.events.emit("app_closed")