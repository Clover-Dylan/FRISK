from ai.ai_engine import AIEngine
from ai.conversation_manager import ConversationManager
from ai.prompt_manager import PromptManager


class Brain:

    def __init__(self):

        self.engine = AIEngine()

        self.conversation = ConversationManager()

        self.prompts = PromptManager()

    def ask(self, prompt):

        self.conversation.add_user(prompt)

        messages = [
            self.prompts.get_system_message(),
            *self.conversation.get_messages()
        ]

        response = self.engine.chat(messages)

        self.conversation.add_assistant(
            response.content
        )

        return response.content

    def clear_memory(self):

        self.conversation.clear()

    def provider_name(self):

        return self.engine.provider.name()

    def set_system_prompt(self, prompt):

        self.prompts.set_prompt(prompt)
    
    def stream(self, prompt):

        self.conversation.add_user(prompt)

        messages = [
            self.prompts.get_system_message(),
            *self.conversation.get_messages()
        ]

        response = ""

        for chunk in self.engine.stream_chat(messages):

            response += chunk

            yield chunk

        self.conversation.add_assistant(response)