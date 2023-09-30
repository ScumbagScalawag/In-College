from common_utils.utils import clearScreen, printOptionList
from common_utils.messages import underConstructionMessage
from pages.new_user_account import printNewAccountScreen

# opens useful links menu, receives and returns currentUser if a login occurs while in this menu
def printGeneralScreen(currentUser=None):
    while True:
        clearScreen()
        # copies default options
        modifiedOptionsList = generalOptionsList
        
        # adds extra sign up option if not signed in already
        if currentUser == None:
            modifiedOptionsList.append("7 - Sign up")
        
        # adds return option everytime, has to do this after sign up to be at bottom
        modifiedOptionsList.append("X - Return to previous menu")

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
        elif userInput == "X":
            break

    return currentUser

generalOptionsList = [
    "*** General ***",
    "1 - Help Center",
    "2 - About",
    "3 - Press",
    "4 - Blog",
    "5 - Careers",
    "6 - Developers"
    ]
#"7 - Sign up", <- appended only if not logged in
#"X - Return to previous menu" <- appended every time

#TODO Clean this up to match other pages
def printHelpCenter():
    clearScreen()
    print(
'''*** Help Center ***
We're here to help!

Press any button to return''')
    userInput = input("")
    return

#TODO Clean this up to match other pages
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

#TODO Clean this up to match other pages
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
    print(underConstructionMessage())
    userInput = input("")
    return
def printCareers():
    print("*** Careers ***")
    print(underConstructionMessage())
    userInput = input("")
    return
def printDevelopers():
    print("*** Developers ***")
    print(underConstructionMessage())
    userInput = input("")
    return
