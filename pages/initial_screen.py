from common_utils.utils import clearScreen, printOptionList
from common_utils.messages import anyButtonToContinueMessage
from pages.friend_search import printFriendSearchScreen
from pages.login import printLoginScreen
from pages.new_user_account import printNewAccountScreen
from pages.link_screens import printUsefulLinkScreen, printImportantLinkScreen
from pages.main_menu import printMainMenu


# Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        printTestimonialPage()
        clearScreen()

        printOptionList(initialScreenOptionsList)

        userInput = input("")

        if userInput == "1":
            # Login as existing user. Go to Login page
            currentUser = printLoginScreen()
            if currentUser != None:
                printMainMenu(currentUser)
        elif userInput == "2":
            # Create a new account. Go to create account page
            currentUser = printNewAccountScreen()
            if currentUser != None:
                printMainMenu(currentUser)
        elif userInput == "3":
            # Search for users
            printFriendSearchScreen()
        elif userInput == "4":
            # Open main menu, login if an account was created at this screen
            currentUser = printUsefulLinkScreen()
            if currentUser != None:
                printMainMenu(currentUser)
        elif userInput == "5":
            # Go to important links page
            printImportantLinkScreen()
        elif userInput.upper() == "X":
            print("Exiting InCollege")
            break
        else:
            print('Invalid selection please input "1" or "2"')
    return 0


def printTestimonialPage():
    printOptionList(testimonialOutputList)
    tempInput = input("")
    return


testimonialOutputList = [
    "*** Welcome to InCollege ***",
    "Here is a story from one of our users:",
    """Hi, my name is Jordan and I have been a huge fan of In-College ever since 
I learned about it through my university. It has been so nice to finally have
a website dedicated to college students, and to be able to connect with all of 
my friends and peers. I even found my first internship through In-College and will
be starting there next month! I can't thank In-College enough for helping me 
succeed in my early career development. """,
    anyButtonToContinueMessage(),
]


initialScreenOptionsList = [
    "*** Welcome to InCollege ***",
    "1 - Login as existing user",
    "2 - Create a new InCollege account",
    "3 - Find InCollege users",
    "4 - Useful Links",
    "5 - InCollege Important Links",
    "X - Close Program",
]
