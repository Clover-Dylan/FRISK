from ai.conversation_manager import ConversationManager


def test_add_message():

    conv = ConversationManager()

    conv.add_user("Hola")

    assert conv.message_count() == 1


def test_clear():

    conv = ConversationManager()

    conv.add_user("Hola")

    conv.clear()

    assert conv.message_count() == 0