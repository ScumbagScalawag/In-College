from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, invalidInputPressToContinue, mustBeLoggedIn
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from pages.friends import printFriendsScreen
from pages.outgoing_friend_requests import printOutgoingFriendRequestsScreen


def printShowMyNetworkScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # if not isLoggedIn(currentUser, "the Show My Network page."):
    #     return currentUser
    if not isinstance(currentUser, User):
        print(mustBeLoggedIn())
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    while True:
        clearScreen()
        printOptionList(showMyNetowrkOptions)
        userInput = input("")

        if userInput == "1":
            currentUser = printFriendsScreen(currentUser)
        elif userInput == "2":
            currentUser = printOutgoingFriendRequestsScreen(currentUser)
            pass
        elif userInput == "3":
            pass
        else:
            invalidInputPressToContinue("1, 2, or X")
            break

    return currentUser


showMyNetowrkOptions = [
    "*** My Network ***",
    "1. View friends List",
    "2. View pending outgoing friend requests",
    # Not strict requirement, but would go here 
    # "3. View pending incomming friend requests",
]