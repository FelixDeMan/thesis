import openai
import json
import os
from pathlib import Path
import sys

from src.agent.utils import SETUP, FEWSHOT, METRICS
from src.agent.colors import Colors


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
        self.metrics = self.load_metrics()

    def validate_instance_directory(self):
        instance_dir = self.script_dir / "memory" / self.instance

        if not instance_dir.exists():
            os.makedirs(instance_dir)

        messages_file = instance_dir / "messages.json"
        metrics_file = instance_dir / "metrics.json"

        if not messages_file.exists():
            with messages_file.open("w") as f:
                json.dump([], f)

        if not metrics_file.exists():
            with metrics_file.open("w") as f:
                json.dump(METRICS, f)

    def load_buffer(self):
        messages_file = self.script_dir / "memory" / self.instance / "messages.json"
        with messages_file.open("r") as f:
            messages = json.load(f)
            return messages[-self.buffer_size :]

    def load_metrics(self):
        metrics_file = self.script_dir / "memory" / self.instance / "metrics.json"
        with metrics_file.open("r") as f:
            metrics = json.load(f)
            return metrics

    def increment_metric(self, metric):
        # Raise an exception if the metrics file or the metric does not exist
        metrics_file = self.script_dir / "memory" / self.instance / "metrics.json"
        with metrics_file.open("r") as f:
            metrics = json.load(f)
            metrics[metric] += 1
        with metrics_file.open("w") as f:
            json.dump(metrics, f)

    def add_message(self, message):
        messages_file = self.script_dir / "memory" / self.instance / "messages.json"
        with messages_file.open("r") as f:
            messages = json.load(f)
            messages.append(message)
        with messages_file.open("w") as f:
            json.dump(messages, f)

        self.buffer = messages[-self.buffer_size :]

    def completion(self, message=None):
        self.increment_metric("invocations")
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

    # Put this in a try catch block
    try:
        content, response = roger.completion(user_message)
    except Exception as e:
        # Print something went wrong with roger in red
        print(
            Colors.RED
            + "Something went wrong with roger. Delete the memory file if this persists."
            + Colors.RESET
        )
        print(e)
        exit()

    assistant_message = {"role": "assistant", "content": content}

    roger.add_message(user_message)
    roger.add_message(assistant_message)

    # print roger in bold blue
    print(Colors.BOLD + Colors.BLUE + "roger: " + Colors.RESET, end="")
    print(content)


if __name__ == "__main__":
    main()
