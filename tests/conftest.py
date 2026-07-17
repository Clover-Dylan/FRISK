import pytest


class FakeProvider:

    model = "fake-model"

    def name(self):
        return "Fake"

    def chat(self, messages):
        return "Respuesta de prueba"


@pytest.fixture
def fake_provider():
    return FakeProvider()