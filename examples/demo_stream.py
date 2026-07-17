from ai import Brain

brain = Brain()

while True:

    text = input("\nTú > ")

    if text == "salir":
        break

    print("\nFRISK >", end=" ", flush=True)

    for chunk in brain.stream(text):

        print(chunk, end="", flush=True)

    print()