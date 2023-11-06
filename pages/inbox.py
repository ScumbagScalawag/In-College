from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, invalidInput
from common_utils.types.message import Message, composeMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printInbox(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase()
    while True:
        userDB.loadUsers()
        # this prints all the messages
        clearScreen()
        printOptionList(inboxOptionsList)
        inboxList = currentUser.incomingMessages

        for number, message in enumerate(inboxList):
            printNumber = "{: <3}".format(number + 1)
            print(f"{printNumber} - {message.header()}")

        # get input for which message to display
        selectedMessage = None
        while True:
            print("Select a message by number or press X to cancel: ", end="")
            selection = input("")
            if selection.lower() == "x":
                break
            try:
                selected_index = int(selection) - 1
                if 0 <= selected_index < len(inboxList):
                    selectedMessage = inboxList[selected_index]
                    break
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print(invalidInput("a whole number or X"))

        # exit if no message was selected
        if selectedMessage == None:
            break

        # invalid input flag so that I can keep message displayed
        flag = 0
        # prints the selected message and options for read/delete/exit
        while True:
            clearScreen()
            print(selectedMessage)
            if flag:
                print(invalidInput("1, 2, or X"))
            printOptionList(messageOptionsList)
            userInput = input("")
            if userInput == "1":
                currentUser.markMessageRead(selected_index)
                userDB.saveDatabase()
                break
            elif userInput == "2":
                currentUser.deleteMessage(selected_index)
                userDB.saveDatabase()
                break
            elif userInput == "X":
                break
            else:
                flag = 1
                continue

        # invalid input flag so that I can keep message displayed
        flag = 0
        # checks if user wants to send a reply and does it if yes
        while True:
            clearScreen()
            print(selectedMessage)
            if flag:
                print(invalidInput("y or n"))
            print("Would you like to send a reply? (y/n): ", end="")
            userInput = input()
            if userInput.lower() == "y":
                sendReply(currentUser, selectedMessage)
                break
            elif userInput.lower() == "n":
                break
            else:
                flag = 1

    return currentUser


inboxOptionsList = [
    "*** Inbox ***",
]

messageOptionsList = [
    "1 - Mark as read",
    "2 - Delete Message",
    "X - Exit",
]


def sendReply(currentUser, selectedMessage):
    newMessage = composeMessage(
        currentUser.username, selectedMessage.sender, currentUser.plusSubscription
    )
    userDB = UserDatabase()
    userDB.loadUsers()
    userDB.addMessage(newMessage)
