import openai
from colors import Colors
import json
import os
from pathlib import Path
import sys
from prompts import SETUP, FEWSHOT


class Roger:
    def __init__(self, buffer_size, instance):
        self.buffer_size = buffer_size
        self.instance = instance
        self.script_dir = Path(__file__).parent.absolute()

        self.validate_instance_directory()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.buffer = self.load_buffer()

        self.setup = SETUP
        self.fewshot_prompts = FEWSHOT

    def validate_instance_directory(self):
        instance_dir = self.script_dir / "memory" / self.instance

        if not instance_dir.exists():
            os.makedirs(instance_dir)

        messages_file = instance_dir / "messages.json"
        if not messages_file.exists():
            with messages_file.open("w") as f:
                json.dump([], f)

    def load_buffer(self):
        messages_file = self.script_dir / "memory" / self.instance / "messages.json"
        with messages_file.open("r") as f:
            messages = json.load(f)
            return messages[-self.buffer_size :]

    def add_message(self, message):
        messages_file = self.script_dir / "memory" / self.instance / "messages.json"
        with messages_file.open("r") as f:
            messages = json.load(f)
            messages.append(message)
        with messages_file.open("w") as f:
            json.dump(messages, f)

        self.buffer = messages[-self.buffer_size :]

    def completion(self, message=None):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": self.setup}]
            + self.fewshot_prompts
            + self.buffer
            + [message],
        )
        content = response["choices"][0]["message"]["content"]

        return content, response


def main():
    roger = Roger(5, "test")

    # Check if there are command line arguments
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input(">>> ")

    user_message = {"role": "user", "content": user_input}

    content, response = roger.completion(user_message)

    assistant_message = {"role": "assistant", "content": content}

    roger.add_message(user_message)
    roger.add_message(assistant_message)

    # print roger in bold blue
    print(Colors.BOLD + Colors.BLUE + "roger: " + Colors.RESET, end="")
    print(content)


if __name__ == "__main__":
    main()
