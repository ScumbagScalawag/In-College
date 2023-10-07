from typing import Optional
from common_utils.messages import (
    anyButtonToContinueMessage,
    convertDictKeysToValidInputString,
    findFriendsRecommendation,
    invalidInputPressToContinue,
    mustBeLoggedIn,
    returnToPreviousMenuMessage,
)

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printFriendsScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # if not isLoggedIn(currentUser, "your friends list."):
    #     return currentUser

    print(currentUser)
    if not isinstance(currentUser, User):
        print(mustBeLoggedIn())
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    userDB = UserDatabase()
    userDB.loadUsers()

    while True:
        clearScreen()
        printOptionList(friendScreenOptions)

        if len(currentUser.friends) < 0:
            print("You currently have no users in your network.", findFriendsRecommendation())
            print(anyButtonToContinueMessage())
            input("")
            break

        friendsDict = {i + 1: friend for i, friend in enumerate(currentUser.friends)}
        print(friendsDict)
        for option, friend in friendsDict.items():
            print(f"{option} - {friend}")
        print(returnToPreviousMenuMessage())

        userInput = input("")
        for option, friend in friendsDict.items():
            if userInput == str(option):
                print(f"userInput = {userInput}")
                print(f"option = {option}")
                # get friend from DB:
                try:
                    user = userDB.getUser(friend)
                    if not isinstance(user, User):
                        raise ValueError(f"User ({friend}) not found")
                except ValueError as e:
                    print(f"Error: {e}")
                    print(anyButtonToContinueMessage())
                    input("")
                    # arguably should break here..
                    continue
                except:
                    print(f"Unknown error occured while retriveing {friend}'s account information")
                    # arguably should break here..
                    continue

                # remove friend
                print("Removing Friend...")
                try:
                    userDB.removeFriend(currentUser, user)
                    print("Friend Removed...")
                    input("")
                except TypeError as e:
                    print(f"Error: {e}")
                    print(anyButtonToContinueMessage())
                    input("")
                    continue
                except:
                    print("Unknown error occured while removing friend")
                    print(anyButtonToContinueMessage())
                    input("")
                    continue
            elif userInput.upper() == "X":
                break
            else:
                # converts options dict to csv of valid options
                validInputCSV = convertDictKeysToValidInputString(friendsDict)
                # Waits for input with interactive csv
                invalidInputPressToContinue(validInputCSV)

    return currentUser


friendScreenOptions = [
    "*** Friends ***",
    "Select User to remove them from your friends list.",
    "Note: This will also remove you from their friends list!\n",
]
