class Message:
    def __init__(self, sender: str, receiver: str, subject="", message="", read=False, plus=False):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.read = read
        self.plus = plus

    # return the Dict translation
    def toDict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "subject": self.subject,
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
            subject=dict.get("subject"),
            message=dict.get("message"),
            read=dict.get("read"),
            plus=dict.get("plus"),
        )

    # return message header
    def header(self):
        if self.read:
            checkBox = "x"
        else:
            checkBox = " "
        return "[{}] From {}: {}".format(checkBox, self.sender, self.subject)

    # return whole message with header and body
    def __str__(self):
        return self.header() + "\n" + self.message

    # change read to true
    def markRead(self):
        self.read = True


def composeMessage(sender, receiver, plus):
    print("Please type your subject (Must be one line):")
    subject = input("")
    bodyList = []
    print(
        "Please type the body of your message, it can be as many lines as you want\nType SEND on its own line at the end when done typing the message"
    )
    newLine = input("")
    while newLine != "SEND":
        bodyList.append(newLine)
        newLine = input("")
    body = ""
    for line in bodyList:
        body = body.strip(" ") + "\n" + line.strip(" ")
    return Message(
        sender,
        receiver,
        subject,
        body,
        False,
        plus,
    )
