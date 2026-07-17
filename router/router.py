from ai import Brain
from router.intents import Intent


class Router:

    def __init__(self, brain: Brain):

        self.brain = brain

    def detect_intent(self, message):

        text = message.lower()

        if text.startswith("abre"):

            return Intent.OPEN_APP

        if any(op in text for op in ["+", "-", "*", "/"]):

            return Intent.CALCULATOR

        return Intent.CHAT

    def route(self, message):

        intent = self.detect_intent(message)

        if intent == Intent.OPEN_APP:

            return "🚧 Automatización próximamente."

        if intent == Intent.CALCULATOR:

            return "🧮 Plugin calculadora próximamente."

        return self.brain.ask(message)