from router.router import Router
from router.intents import Intent


class FakeBrain:

    def ask(self, prompt):
        return "OK"


def test_chat():

    router = Router(FakeBrain())

    assert router.detect_intent("Hola") == Intent.CHAT


def test_open():

    router = Router(FakeBrain())

    assert router.detect_intent("abre chrome") == Intent.OPEN_APP


def test_calculator():

    router = Router(FakeBrain())

    assert router.detect_intent("2+2") == Intent.CALCULATOR