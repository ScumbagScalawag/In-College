from common_utils.utils import clearScreen
from pages.login import printLoginScreen
from pages.new_user_account import printNewAccountScreen


# Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        print("*** Welcome to InCollege ***")
        print("1 - Login as existing user")
        print("2 - Create a new InCollege account")

        userInput = input()

        if userInput == "1":
            # Login as existing user. Go to Login page
            printLoginScreen()
            break
        elif userInput == "2":
            # Create a new account. Go to create account page
            printNewAccountScreen()
            break
        else:
            print('Invalid selection please input "1" or "2"')
    return
