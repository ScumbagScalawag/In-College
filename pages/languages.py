from typing import Optional

from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInput,
    returnToPreviousMenuMessage,
)
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printLanguagesScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # if not logged in:
    if not isinstance(currentUser, User):
        while True:
            clearScreen()
            printOptionList(languageLoggedOutOptions)
            userInput = input("")

            if userInput.upper() == "X":
                break
            else:
                print(invalidInput("X"))
                print(anyButtonToContinueMessage())
                input("")

    # if logged in:
    if isinstance(currentUser, User):
        userDB = UserDatabase([])
        userDB.loadUsers()

        while True:
            clearScreen()
            printOptionList(languageLoggedInOptions)
            print("Your current language is", currentUser.language)
            userInput = input("")

            if userInput == "1":
                # update currentUsers info (in mem) AND DB (json)
                currentUser.setLanguage("English")
                userDB.updateUser(currentUser)
            elif userInput == "2":
                currentUser.setLanguage("Spanish")
                userDB.updateUser(currentUser)
            elif userInput.upper() == "X":
                break
            else:
                print(invalidInput("1, 2, or X"))
                print(anyButtonToContinueMessage())
                input("")

    return currentUser


languageLoggedOutOptions = [
    "*** Languages ***",
    "Please log in to change language settings",
    returnToPreviousMenuMessage(),
]

languageLoggedInOptions = [
    "*** Languages ***",
    "Select your preferred language:",
    "1 - English",
    "2 - Spanish",
    returnToPreviousMenuMessage(),
]
