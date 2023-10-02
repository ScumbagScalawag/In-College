from typing import Optional
from common_utils.messages import anyButtonToContinueMessage, invalidInput, returnToPreviousMenuMessage
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from pages.privacy_policy import printPrivacyPolicyPage


# opens important links menu
def printImportantLinkScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(importantLinksOptionsList)
        userInput = input("")

        if userInput == "1":
            continue
        elif userInput == "2":
            continue
        elif userInput == "3":
            continue
        elif userInput == "4":
            continue
        elif userInput == "5":
            currentUser = printPrivacyPolicyPage(currentUser)
            continue
        elif userInput == "6":
            continue
        elif userInput == "7":
            continue
        elif userInput == "8":
            continue
        elif userInput == "9":
            continue
        elif userInput == "10":
            continue
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or X"))
            print(anyButtonToContinueMessage())
            input("")
    return currentUser


importantLinksOptionsList = [
    "*** InCollege Important Links ***",
    "1 - A Copyright Notice",
    "2 - About",
    "3 - Accessibility",
    "4 - User Agreement",
    "5 - Privacy Policy",
    "6 - Cookie Policy",
    "7 - Copyright Policy",
    "8 - Brand Policy",
    "9 - Guest Controls",
    "10 - Languages",
    returnToPreviousMenuMessage(),
]
