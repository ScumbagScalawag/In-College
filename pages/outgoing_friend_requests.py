from typing import Optional
from common_utils.messages import (
    anyButtonToContinueMessage,
    convertDictKeysToValidInputString,
    findFriendsRecommendation,
    invalidInputPressToContinue,
    mustBeLoggedIn,
    returnToPreviousMenuReducedMessage,
)

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printOutgoingFriendRequestsScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # if not isLoggedIn(currentUser, "the Show My Network page."):
    #     return currentUser
    if not isinstance(currentUser, User):
        print(mustBeLoggedIn())
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    userDB = UserDatabase()
    userDB.loadUsers()

    while True:
        clearScreen()
        printOptionList(outgoingFriendRequestOptions)

        if len(currentUser.friends) <= 0:
            print("You currently have no outgoing friend requests.", findFriendsRecommendation())
            print(anyButtonToContinueMessage())
            input("")
            break

        # print pending friend requests options
        friendsDict = {str(i + 1): friend for i, friend in enumerate(currentUser.friendRequests)}
        friendsDict["X"] = returnToPreviousMenuReducedMessage()
        if len(friendsDict) > 0:
            for option, friend in friendsDict.items():
                print(f"{option} - {friend}")
        else:
            pass

        userInput = input("")
        option = "UNKNOWN"
        friend = "UNKNOWN"

        # ability to "Unsend" Friend request would go here, if required
        if userInput.upper() == "X":
            break
        else:
            # No interactive selection actions yet, so options are "unclickable"
            # validInputCSV = convertDictKeysToValidInputString(friendsDict)
            # invalidInputPressToContinue(validInputCSV)
            invalidInputPressToContinue("X")
            continue

    return currentUser


outgoingFriendRequestOptions = ["*** Outgoing Friend Requests ***"]
