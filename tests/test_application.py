from core.application import Application


def test_application_creation():

    app = Application()

    assert app.get("logger") is not None

    assert app.get("events") is not None