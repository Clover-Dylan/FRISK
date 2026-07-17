from ai.prompt_manager import PromptManager


def test_prompt_exists():

    manager = PromptManager()

    assert manager.get_prompt() != ""


def test_change_prompt():

    manager = PromptManager()

    manager.set_prompt("Nuevo prompt")

    assert manager.get_prompt() == "Nuevo prompt"