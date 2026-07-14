from typing import Any


class ServiceContainer:
    """
    Contenedor de servicios de FRISK.

    Se encarga de registrar y devolver instancias
    compartidas en toda la aplicación.
    """

    def __init__(self):

        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:

        if name in self._services:
            raise ValueError(f"El servicio '{name}' ya está registrado.")

        self._services[name] = service

    def get(self, name: str) -> Any:

        if name not in self._services:
            raise KeyError(f"Servicio '{name}' no encontrado.")

        return self._services[name]

    def exists(self, name: str) -> bool:

        return name in self._services

    def remove(self, name: str) -> None:

        if name in self._services:
            del self._services[name]

    def list_services(self) -> list[str]:

        return sorted(self._services.keys())