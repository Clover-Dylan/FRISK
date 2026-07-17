from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Clase base para cualquier proveedor de IA.
    """

    @abstractmethod
    def chat(self, messages: list[dict]) -> str:
        """
        Envía una conversación al modelo y devuelve la respuesta.
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """
        Nombre del proveedor.
        """
        pass