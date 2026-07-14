from core.service_container import ServiceContainer


def test_register_service():

    container = ServiceContainer()

    obj = object()

    container.register("test", obj)

    assert container.get("test") is obj


def test_exists():

    container = ServiceContainer()

    container.register("logger", object())

    assert container.exists("logger")


def test_remove():

    container = ServiceContainer()

    container.register("logger", object())

    container.remove("logger")

    assert not container.exists("logger")