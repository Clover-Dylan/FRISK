from core.application import Application


class Assistant:

    def __init__(self, app: Application):

        self.app = app

        self.logger = app.get("logger")

        self.router = app.get("router")

    def start(self):

        self.logger.info("Assistant iniciado.")

        self.app.start()

    def stop(self):

        self.logger.info("Assistant detenido.")

        self.app.stop()

    def process_message(self, message):

        return self.router.route(message)