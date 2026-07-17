from ai.brain import Brain


class FakeResponse:

    def __init__(self):

        self.content = "Hola"


class FakeEngine:

    def chat(self, messages):

        return FakeResponse()


def test_brain():

    brain = Brain(engine=FakeEngine())

    assert brain.ask("Hola") == "Hola"