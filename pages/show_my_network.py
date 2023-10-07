from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, mustBeLoggedIn
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from pages.friends import printFriendsScreen


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
        if userInput == "2":
            if len(currentUser.friendRequests) > 0:
                print("\n*** Outgoing Friend Requests ***")
                print("Select user to unsend the friend request.")
                friendsDict = {i + 1: friend for i, friend in enumerate(currentUser.friends)}
                for option, friend in friendsDict.items():
                    print(f"{option} - {friend}")
            else:
                print("")
        if userInput == "3":
            break

    return currentUser


showMyNetowrkOptions = [
    "*** My Network ***",
    "1. View friends List",
    "2. View pending outgoing friend requests",
    "3. View pending incomming friend requests",
]
