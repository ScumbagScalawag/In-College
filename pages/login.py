from common_utils.utils import clearScreen
from common_utils.utils import loadUsers
from pages.main_menu import printMainMenu

MAX_LOGIN_ATTEMPTS = 5


# Menu: Login to user account
def printLoginScreen():
    # To Do
    clearScreen()
    user = loadUsers()
    # not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later
    loginAttempts = 0

    while True:
        print(" Login to InCollege ")
        print("Username: ", end="")
        username = input()
        print("Password: ", end="")
        password = input()
        # User input recieved

        # match username and password
        if checkLoginInfo(user, username, password):  # and loginAttempts <= maximum attempts allowed
            # Valid Login
            print("You have successfully logged in")
            printMainMenu()
            return
        else:
            # Invalid Login
            print("Incorret username / password, please try again")
            loginAttempts = loginAttempts + 1

            # TODO: Enforce max login attempts (not required afaik) -noah
            # if loginAttempts >= MAX_LOGIN_ATTEMPTS:
            #     break

    return


# Helper: Used in login to check if valid login information
# NOTE: made this function have "user" as an input so we don't have to
# have a global user (dependency injection) -noah
def checkLoginInfo(user, username, password):
    for i in user:
        if i == username and user[i] == password:
            return True
    return False  # Not Found
