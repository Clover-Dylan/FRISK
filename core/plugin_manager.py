import importlib
import inspect
import pkgutil

from plugins.plugin_base import Plugin


class PluginManager:

    def __init__(self):
        self.plugins = []
        self.load_plugins()

    def load_plugins(self):

        import plugins

        for _, module_name, _ in pkgutil.iter_modules(plugins.__path__):

            if module_name == "plugin_base":
                continue

            module = importlib.import_module(f"plugins.{module_name}")

            for _, obj in inspect.getmembers(module, inspect.isclass):

                # Solo cargar clases definidas en este módulo
                if obj.__module__ != module.__name__:
                    continue

                # Debe heredar de Plugin
                if not issubclass(obj, Plugin):
                    continue

                # No cargar la clase base
                if obj is Plugin:
                    continue

                self.plugins.append(obj())

    def execute(self, command):

        for plugin in self.plugins:

            if plugin.can_handle(command):
                return plugin.execute(command)

        return None