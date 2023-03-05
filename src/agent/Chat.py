import openai
import os
from typing import List, Tuple, Optional
from Message import Message


class Chat:
    """
    A class representing a chat session between a user and a terminal assistant.

    Attributes:
        buffer_size (Optional[int]): The maximum number of messages to keep in the chat history, or None if no buffer is used.
        messages (Optional[List[Message]]): The current state of the chat history, or None if no buffer is used.
    """

    setup = "You are roger, a MacOS terminal assistant that helps users with various tasks on the terminal. You can answer questions, provide code, and ask for specifics such as paths and system info, you can ask users to run a command and to show you the output to aid your reasoning. In cases where you must show commands, you must output all commands in an ordered JSON format containing one or more commands. Assume that you are asked for shell commands unless explicitly told to show another language. You talk in a very precise and technical manner."

    def __init__(self, buffer_size: int = None) -> None:
        """
        Initializes a new Chat object with the specified buffer size, or no buffer if buffer_size is None.

        Args:
            buffer_size (Optional[int]): The maximum number of messages to keep in the chat history, or None if no buffer is used.

        Returns:
            None
        """
        self.buffer_size: Optional[int] = buffer_size
        self.messages: Optional[List[Message]] = None if buffer_size is None else []
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def add_message(self, message: Tuple[str, str], assistant=False) -> None:
        """
        Adds a new chat entry to the chat history, if one is being used.

        Args:
            entry (Tuple[str, str]): A tuple representing a new chat entry, where the first element is the message
                                     and the second element is the sender.

        Returns:
            None
        """
        role = "user" if not assistant else "assistant"
        message = {"role": role, "content": message}

        if self.messages is not None:
            self.messages.append(message)
            if len(self.messages) > self.buffer_size:
                self.messages.pop(0)

    def get_messages(self) -> Optional[List[Tuple[str, str]]]:
        """
        Returns the current state of the chat history, or None if no buffer is being used.

        Returns:
            Optional[List[Tuple[str, str]]]: A list of tuples representing the chat history, where each tuple contains
                                              two strings representing a chat message and its sender, or None if
                                              no buffer is being used.
        """
        return self.messages

    def completion(self, message=None):
        """
        Completes the given message using the OpenAI API.

        Args:
            message (Optional[str]): The message to be completed. If None, the setup message is used.

        Returns:
            None
        """
        body = self.messages if self.messages else []
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": self.setup}] + body + [message],
        )

        completion = response["choices"][0]["message"]["content"]

        return completion, response


def main():
    """
    The main function for running the terminal assistant.
    """
    chat = Chat()
    message = Message(input("User >>> "), assistant=False).message["content"]
    completion, response = chat.completion(
        message=Message(message, assistant=False).message
    )

    print("Roger >>> " + completion)


if __name__ == "__main__":
    main()
