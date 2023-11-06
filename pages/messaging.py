from typing import Optional

from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInput,
    returnToPreviousMenuMessage,
    returnToPreviousMenuReducedMessage,
)
from common_utils.types.message import Message, composeMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList
from pages.inbox import printInbox


def printMessagingScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(messagingOptionsList)
        userInput = input("")
        if userInput == "1":
            printNewMessage(currentUser)
        elif userInput == "2":
            printInbox(currentUser)
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, or X"))
    return currentUser


messagingOptionsList = [
    "*** InCollege Messaging ***",
    "1 - New Message",
    "2 - Inbox",
    returnToPreviousMenuMessage(),
]


def printNewMessage(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(newMessageOptionsList)
        userInput = input("")
        if userInput == "1":
            recipient = chooseByName(currentUser)
        elif userInput == "2":
            recipient = chooseFromFriends(currentUser)
        elif userInput == "3":
            if currentUser.plusSubscription:
                recipient = chooseFromAll()
            else:
                print("That feature is only available for InCollege Plus members")
                print(anyButtonToContinueMessage())
                input("")
                continue
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, 3, or X"))
            print(anyButtonToContinueMessage())
            input("")
            continue
        # detect if any of the submenus were exited, skip message creation if no recipient specified
        if recipient == None:
            continue
        clearScreen()
        print("*** New Message ***")
        print("Recipient:", recipient)
        # use recipient to compose message
        newMessage = composeMessage(currentUser.username, recipient, currentUser.plusSubscription)
        # give that message to database to put it in inbox of other user
        userDB = UserDatabase()
        userDB.loadUsers()
        userDB.addMessage(newMessage)
    return currentUser


newMessageOptionsList = [
    "*** New Message ***",
    "1 - Choose a recipient by name",
    "2 - Choose from all friends",
    "3 - Choose from all members (InCollege Plus exclusive)",
    returnToPreviousMenuMessage(),
]


# asks user to input a username, checks for validity, returns that username as recipient
def chooseByName(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        # get input
        clearScreen()
        print("*** New Message ***")
        print("Enter username of user you would like to message, or X to return to previous menu")
        userInput = input("")
        if userInput == "X":
            return None

        # load userDB so we can search for user
        userDB = UserDatabase()
        userDB.loadUsers()

        # validate: user must exist
        if not userDB.userExists(userInput):
            print("User is not in the InCollege system")
            print(anyButtonToContinueMessage())
            input("")
            continue
        # validate: it must be a friend OR user must a Plus member
        elif not currentUser.isFriend(userInput) and not currentUser.plusSubscription:
            print("I'm sorry, you are not friends with that person")
            print(anyButtonToContinueMessage())
            input("")
            continue
        else:
            # if it passed all the validation, pass it on
            return userInput


# displays friends list, lets user choose one, returns that username as recipient
def chooseFromFriends(currentUser: Optional[User] = None) -> Optional[User]:
    # load userDB so we can search for users
    userDB = UserDatabase()
    userDB.loadUsers()

    # add all usernames from friends list to an options list
    friendsDict = {str(i + 1): friend for i, friend in enumerate(currentUser.friends)}
    friendsDict["X"] = returnToPreviousMenuReducedMessage()
    # enter display loop
    while True:
        # header
        clearScreen()
        print("*** New Message ***")
        # check if empty
        if len(currentUser.friends) <= 0:
            print("You currently have no users in your network")
            print(anyButtonToContinueMessage())
            input("")
            return None
        print("Select a friend to message")

        # display options list
        if len(friendsDict) > 0:
            for option, friend in friendsDict.items():
                print(f"{option} - {friend}")

        # get input
        print("")
        userInput = input("")

        if userInput.upper() == "X":
            return None
        elif userInput in friendsDict:
            return friendsDict[userInput]
        else:
            print(invalidInput("a shown whole number or X"))
            print(anyButtonToContinueMessage())
            input("")
            continue


# displays all users, lets user choose one, returns that username as recipient
def chooseFromAll(currentUser: Optional[User] = None) -> Optional[User]:
    # load userDB so we can search for users
    userDB = UserDatabase()
    userDB.loadUsers()

    # add all usernames from userDB to an options list
    i = 1
    usersDict = {}
    for user in userDB.userlist:
        if user.username == currentUser.username:
            continue
        usersDict[str(i)] = user.username
        i += 1
    usersDict["X"] = returnToPreviousMenuReducedMessage()

    # enter display loop
    while True:
        # header
        clearScreen()
        print("*** New Message ***")
        print("Select a user to message")

        # display options list
        if len(usersDict) > 0:
            for option, friend in usersDict.items():
                print(f"{option} - {friend}")

        # get input
        print("")
        userInput = input("")

        if userInput.upper() == "X":
            return None
        elif userInput in usersDict:
            return usersDict[userInput]
        else:
            print(invalidInput("a shown whole number or X"))
            print(anyButtonToContinueMessage())
            input("")
            continue
