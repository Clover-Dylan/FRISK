from collections import defaultdict
from typing import Callable, Any


class EventBus:
    """
    Sistema de eventos de FRISK.

    Permite que cualquier módulo emita eventos y que otros
    módulos se suscriban para reaccionar a ellos.
    """

    def __init__(self):

        self._listeners = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable[..., Any]) -> None:
        """
        Registrar un listener para un evento.
        """

        self._listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable[..., Any]) -> None:
        """
        Eliminar un listener.
        """

        if callback in self._listeners[event_name]:
            self._listeners[event_name].remove(callback)

    def emit(self, event_name: str, *args, **kwargs) -> None:
        """
        Disparar un evento.
        """

        for callback in self._listeners[event_name]:
            callback(*args, **kwargs)

    def listeners(self, event_name: str) -> int:
        """
        Devuelve cuántos listeners tiene un evento.
        """

        return len(self._listeners[event_name])

    def clear(self) -> None:
        """
        Elimina todos los eventos registrados.
        """

        self._listeners.clear()