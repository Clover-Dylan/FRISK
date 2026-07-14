from groq import Groq

from ai.models import AIModels
from ai.prompt import SYSTEM_PROMPT
from ai.conversation import Conversation

from config.settings import API_KEY


class Brain:

    def __init__(self):

        self.client = Groq(api_key=API_KEY)

        self.conversation = Conversation()

        self.conversation.add("system", SYSTEM_PROMPT)

    def ask(self, text):

        self.conversation.add("user", text)

        try:

            response = self.client.chat.completions.create(
                model=AIModels.PRIMARY,
                messages=self.conversation.history()
            )

        except Exception:

            response = self.client.chat.completions.create(
                model=AIModels.BACKUP,
                messages=self.conversation.history()
            )

        answer = response.choices[0].message.content

        self.conversation.add("assistant", answer)

        return answer