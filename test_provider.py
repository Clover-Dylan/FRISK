from ai.providers import ProviderFactory

provider = ProviderFactory.create()

print()

print("Proveedor:")

print(provider.name())

messages = [

    {
        "role": "user",
        "content": "Di solamente: Hola Dylan."
    }

]

response = provider.chat(messages)

print()

print(response)