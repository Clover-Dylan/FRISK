from plugins.plugin_base import Plugin

class CalculatorPlugin(Plugin):

    def can_handle(self, command):

        return command.lower().startswith("calcula ")

    def execute(self, command):

        expression = command[9:]

        try:

            result = eval(expression)

            return f"El resultado es {result}"

        except Exception:

            return "No pude calcular esa operación."