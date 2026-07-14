from core import Application, Assistant
from config import APP_NAME


def main():

    print("=" * 50)
    print(APP_NAME)
    print("=" * 50)

    app = Application()

    assistant = Assistant(app)

    assistant.start()

    while True:

        try:

            message = input("\nTú > ").strip()

            if not message:
                continue

            if message.lower() in (
                "salir",
                "exit",
                "quit"
            ):
                break

            response = assistant.process_message(message)

            print(f"\nFRISK > {response}")

        except KeyboardInterrupt:

            print("\n")

            break

        except Exception as error:

            logger = app.get("logger")

            logger.error(str(error))

            print("\nHa ocurrido un error.")

    assistant.stop()


if __name__ == "__main__":
    main()