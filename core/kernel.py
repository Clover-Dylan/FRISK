from core.logger import Logger
from core.service_container import ServiceContainer


class Kernel:

    def __init__(self):

        self.container = ServiceContainer()

        logger = Logger()

        self.container.register("logger", logger)

        logger.info("Kernel iniciado.")

    @property
    def logger(self):

        return self.container.get("logger")