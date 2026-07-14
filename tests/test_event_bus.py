from core.event_bus import EventBus


def test_event_execution():

    bus = EventBus()

    executed = False

    def callback():

        nonlocal executed

        executed = True

    bus.subscribe("start", callback)

    bus.emit("start")

    assert executed