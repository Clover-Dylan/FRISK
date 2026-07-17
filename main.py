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

        text = input("\nTú > ")

        if text.lower() == "salir":

            break

        answer = assistant.process_message(text)

        print()

        print("FRISK >", answer)

    assistant.stop()


if __name__ == "__main__":

    main()