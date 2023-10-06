from typing import Optional
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from common_utils.messages import (
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from pages.links_general import printGeneralScreen

# opens useful links menu, receives and returns currentUser if a login occurs while in this menu
def printUsefulLinkScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(usefulLinksOptionsList)
        userInput = input("")

        if userInput == "1":
            currentUser = printGeneralScreen(currentUser)
            if currentUser != None:
                break
        elif userInput == "2":
            currentUser = printBrowseInCollege(currentUser)
        elif userInput == "3":
            currentUser = printBusinessSolutions(currentUser)
        elif userInput == "4":
            currentUser = printDirectories(currentUser)
        elif userInput.upper() == "X":
            break

    return currentUser


def printBrowseInCollege(currentUser: Optional[User] = None) -> Optional[User]:
    print("*** Browse InCollege ***")
    print(underConstructionMessage())
    input("")
    return currentUser


def printBusinessSolutions(currentUser: Optional[User] = None) -> Optional[User]:
    print("*** Business Solutions ***")
    print(underConstructionMessage())
    input("")
    return currentUser


def printDirectories(currentUser: Optional[User] = None) -> Optional[User]:
    print("*** Directories ***")
    print(underConstructionMessage())
    input("")
    return currentUser


usefulLinksOptionsList = [
    "*** Useful Links ***",
    "1 - General",
    "2 - Browse InCollege",
    "3 - Business Solutions",
    "4 - Directories",
    returnToPreviousMenuMessage(),
]
