from common_utils.utils import clearScreen, userSearch, loadUsers
from pages.main_menu import printMainMenu

MAX_LOGIN_ATTEMPTS = 5


# Menu: Login to user account
def printLoginScreen():
    # To Do
    users = loadUsers()
    # not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later
    loginAttempts = 0

    while True:
        clearScreen()
        print(" Login to InCollege ")
        print("Username: ", end="")
        username = input()
        print("Password: ", end="")
        password = input()
        # User input recieved

        # match username and password
        userIndex = userSearch(users, username=username, password=password, returnIndex=True)
        if userIndex != False:  # and loginAttempts <= maximum attempts allowed
            # Valid Login
            print("You have successfully logged in")
            printMainMenu(userIndex)
            return
        else:
            # Invalid Login
            print("Incorrect username / password, please try again")
            loginAttempts = loginAttempts + 1
            while True:
                confirm = input("Input c to continue or x to return to menu: ")
                if confirm.upper() == "X":
                    return
                elif confirm.upper() == "C":
                    break
            
            # TODO: Enforce max login attempts (not required afaik) -noah
            # if loginAttempts >= MAX_LOGIN_ATTEMPTS:
            #     break

    return
