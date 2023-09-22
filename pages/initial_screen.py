from common_utils.utils import clearScreen
from pages.friend_search import printFriendSearchScreen
from pages.login import printLoginScreen
from pages.new_user_account import printNewAccountScreen


# Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        print("*** Welcome to InCollege ***")
        print("Here is a story from one of our users:")
        print(
            """Hi, my name is Jordan and I have been a huge fan of In-College ever since 
              I learned about it.. 
              """
        )

        print("Press any button to continue")
        tempInput = input()
        clearScreen()

        print("*** Welcome to InCollege ***")
        print("1 - Login as existing user")
        print("2 - Create a new InCollege account")
        print("3 - Find InCollege users")
        print("X - Close Program")

        userInput = input()

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
