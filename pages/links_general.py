from common_utils.utils import clearScreen, printOptionList
from pages.new_user_account import printNewAccountScreen
from pages.under_construction import underConstructionMessage

# opens useful links menu, receives and returns currentUser if a login occurs while in this menu
def printGeneralScreen(currentUser=None):
    while True:
        clearScreen()
        printOptionList(generalOptionsList)
        userInput = input("")

        if userInput == "1":
            currentUser = printNewAccountScreen()
            if currentUser != None:
                break
        elif userInput == "2":
            printHelpCenter()
        elif userInput == "3":
            printAbout()
        elif userInput == "4":
            printPress()
        elif userInput == "5":
            continue
        elif userInput == "6":
            continue
        elif userInput == "7":
            continue
        elif userInput == "X":
            break

    return currentUser

generalOptionsList = [
    "*** General ***",
    "1 - Sign up",
    "2 - Help Center",
    "3 - About",
    "4 - Press",
    "5 - Blog",
    "6 - Careers",
    "7 - Developers",
    "X - Return to previous menu"
]

def printHelpCenter():
    clearScreen()
    print(
'''*** Help Center ***
We're here to help!

Press any button to return''')
    userInput = input("")
    return

def printAbout():
    clearScreen()
    print(
'''*** About ***
In College: Welcome to In College, the world's largest
college student network with many users in many countries
and territories worldwide

Press any button to return'''
    )
    userInput = input("")
    return

def printPress():
    clearScreen()
    print(
'''*** Press ***
In College Pressroom: Stay on top of the latest
news, updates, and reports

Press any button to return'''
    )
    userInput = input("")
    return

def printBlog():
    print("*** Blog ***")
    print(underConstructionMessage)
    userInput = input("")
    return
def printCareers():
    print("*** Careers ***")
    print(underConstructionMessage)
    userInput = input("")
    return
def printDevelopers():
    print("*** Developers ***")
    print(underConstructionMessage)
    userInput = input("")
    return