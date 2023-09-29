from common_utils.utils import clearScreen, printOptionList
from pages.new_user_account import printNewAccountScreen
from pages.links_general import printGeneralScreen
from pages.under_construction import underConstructionMessage

# WIP none of the buttons do anything yet
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
def printImportantLinkScreen():
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
        elif userInput == "X":
            break

    return 0

def printBrowseInCollege():
    print("*** Browse InCollege ***")
    print(underConstructionMessage)
    userInput = input("")
    return
def printBusinessSolutions():
    print("*** Business Solutions ***")
    print(underConstructionMessage)
    userInput = input("")
    return
def printDirectories():
    print("*** Directories ***")
    print(underConstructionMessage)
    userInput = input("")
    return

usefulLinksOptionsList = [
    "*** Useful Links ***",
    "1 - General",
    "2 - Browse InCollege",
    "3 - Business Solutions",
    "4 - Directories",
    "X - Return to previous menu"
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
    "X - Return to previous menu"
]