from typing import Optional
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from common_utils.messages import (
    anyButtonToContinueMessage,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from pages.new_user_account import printNewAccountScreen


# opens useful links menu, receives and returns currentUser if a login occurs while in this menu
def printGeneralScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        # copies default options
        modifiedOptionsList = generalOptionsList

        # adds extra sign up option if not signed in already
        if currentUser == None:
            modifiedOptionsList.append("7 - Sign up")

        # adds return option everytime, has to do this after sign up to be at bottom
        modifiedOptionsList.append(returnToPreviousMenuMessage())

        # print menu
        printOptionList(modifiedOptionsList)
        userInput = input("")

        # process input
        if userInput == "1":
            printHelpCenter()
        elif userInput == "2":
            printAbout()
        elif userInput == "3":
            printPress()
        elif userInput == "4":
            printBlog()
        elif userInput == "5":
            printCareers()
        elif userInput == "6":
            printDevelopers()
        # option only available in logged out mode
        elif userInput == "7" and currentUser == None:
            currentUser = printNewAccountScreen()
            if currentUser != None:
                break
        elif userInput.upper() == "X":
            break

    return currentUser


generalOptionsList = [
    "*** General ***",
    "1 - Help Center",
    "2 - About",
    "3 - Press",
    "4 - Blog",
    "5 - Careers",
    "6 - Developers",
]
# "7 - Sign up", <- appended only if not logged in
# "X - Return to previous menu" <- appended every time


def printHelpCenter(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    printOptionList(helpOptions)
    userInput = input("")
    return currentUser


helpOptions = ["*** Help Center ***", "We're here to help!", "\n", anyButtonToContinueMessage()]


def printAbout(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    printOptionList(aboutOptions)
    userInput = input("")
    return currentUser


aboutOptions = [
    "*** About ***",
    """In College: Welcome to In College, the world's largest
    college student network with many users in many countries
    and territories worldwide\n""",
    anyButtonToContinueMessage(),
]


def printPress(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    printOptionList(pressOptions)
    userInput = input("")
    return currentUser


pressOptions = [
    "*** Press ***",
    """In College Pressroom: Stay on top of the latest
    news, updates, and reports\n""",
    anyButtonToContinueMessage(),
]


def printBlog(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(blogOptions)
    userInput = input("")
    return currentUser


blogOptions = ["*** Blog ***\n", underConstructionMessage()]


def printCareers(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(careersOptions)
    userInput = input("")
    return currentUser


careersOptions = ["*** Careers ***\n", underConstructionMessage()]


def printDevelopers(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(developersOptions)
    userInput = input("")
    return currentUser


developersOptions = ["*** Developers ***\n", underConstructionMessage()]
