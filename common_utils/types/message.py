class Message:
    def __init__(self, sender: str, receiver: str, message="", read=False, plus=False):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.read = read
        self.plus = plus

    # return the Dict translation
    def toDict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message,
            "read": self.read,
            "plus": self.plus,
        }

    # create a Message object from a Dict
    @classmethod
    def dictToMessage(self, dict):
        return self(
            sender=dict.get("sender"),
            receiver=dict.get("receiver"),
            message=dict.get("message"),
            read=dict.get("read"),
            plus=dict.get("plus"),
        )
