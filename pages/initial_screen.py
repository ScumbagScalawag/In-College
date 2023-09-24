from common_utils.utils import clearScreen
from pages.friend_search import printFriendSearchScreen
from pages.login import printLoginScreen
from pages.new_user_account import printNewAccountScreen


# Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        printTestimonialPage()
        clearScreen()

        options = initialScreenOptionsList
        for option in options:
            print(option)

        userInput = input("")

        if userInput == "1":
            # Login as existing user. Go to Login page
            printLoginScreen()
        elif userInput == "2":
            # Create a new account. Go to create account page
            printNewAccountScreen()
        elif userInput == "3":
            # Search for users
            printFriendSearchScreen()
        elif userInput.upper() == "X":
            print("Exiting InCollege")
            break
        else:
            print('Invalid selection please input "1" or "2"')
    return 0


testimonialOutputList = [
    "*** Welcome to InCollege ***",
    "Here is a story from one of our users:",
    """Hi, my name is Jordan and I have been a huge fan of In-College ever since 
I learned about it through my university. It has been so nice to finally have
a website dedicated to college students, and to be able to connect with all of 
my friends and peers. I even found my first internship through In-College and will
be starting there next month! I can't thank In-College enough for helping me 
succeed in my early career development. """,
    "Press any button to continue",
]


def printTestimonialPage():
    for output in testimonialOutputList:
        print(output)
    tempInput = input("")
    return

initialScreenOptionsList = [
        "*** Welcome to InCollege ***",
        "1 - Login as existing user",
        "2 - Create a new InCollege account",
        "3 - Find InCollege users",
        "X - Close Program",
    ]
