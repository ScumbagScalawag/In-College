from common_utils.utils import clearScreen, printOptionList
from common_utils.messages import (
    invalidInput,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from pages.links_general import printGeneralScreen
from pages.privacy_policy import printPrivacyPolicyPage

# TODO: 1. Split up link_screen into its respective pages
# TODO: 2. Fix the test imports for new pages once


# opens useful links menu, receives and returns currentUser if a login occurs while in this menu
def printUsefulLinkScreen(currentUser=None):
    while True:
        clearScreen()
        printOptionList(usefulLinksOptionsList)
        userInput = input("")

        if userInput == "1":
            currentUser = printGeneralScreen()
            if currentUser != None:
                break
        elif userInput == "2":
            printBrowseInCollege()
        elif userInput == "3":
            printBusinessSolutions()
        elif userInput == "4":
            printDirectories()
        elif userInput == "X":
            break

    return currentUser


# opens important links menu
def printImportantLinkScreen(currentUser=None):
    while True:
        clearScreen()
        print("-----printImportantLinkScreen")
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
            printPrivacyPolicyPage(currentUser)
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
            invalidInput("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or X")
        # TODO: Invalid Input
    return 0


def printBrowseInCollege():
    print("*** Browse InCollege ***")
    print(underConstructionMessage())
    userInput = input("")
    return


def printBusinessSolutions():
    print("*** Business Solutions ***")
    print(underConstructionMessage())
    userInput = input("")
    return


def printDirectories():
    print("*** Directories ***")
    print(underConstructionMessage())
    userInput = input("")
    return


usefulLinksOptionsList = [
    "*** Useful Links ***",
    "1 - General",
    "2 - Browse InCollege",
    "3 - Business Solutions",
    "4 - Directories",
    returnToPreviousMenuMessage(),
]

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
