class Message:
    """
    A class representing a message in a conversation.

    Attributes:
        message (str): The content of the message.
        assistant (bool): A flag indicating whether the message was sent by an assistant.
                          If True, the message is from the assistant, otherwise it is from the user.
    """

    def __init__(self, message: str, role: str = "assistant") -> dict:
        """
        Initializes a new Message object.

        Args:
            message (str): The content of the message.
            assistant (bool): A flag indicating whether the message was sent by an assistant.
                              If True, the message is from the assistant, otherwise it is from the user.

        Returns:
            dict: A dictionary with two keys: "role" and "content".
                  The "role" key's value is either "assistant" or "user" depending on the value of the assistant parameter.
                  The "content" key's value is the message passed to the constructor.
        """
        self.role = role
        self.content = message
        if role == "assistant":
            self.message = {"role": "assistant", "content": message}
        elif role == "user":
            self.message = {"role": "user", "content": message}

    def to_json(self) -> str:
        """
        Returns a JSON-serializable dictionary representation of the object.
        """
        return {"role": self.role, "content": self.content}
