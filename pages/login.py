from typing import Optional

from common_utils.messages import (
    alreadyLoggedIn,
    anyButtonToContinueMessage,
    invalidInput,
)
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from common_utils.utils import clearScreen
from pages.inbox import printInbox

MAX_LOGIN_ATTEMPTS = 5


# Menu: Login to user account
def printLoginScreen(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()
    # To Do
    # not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later

    # exit if logged in
    if isinstance(currentUser, User):
        print(alreadyLoggedIn("Please log out and log back in to change accounts"))
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    loginAttempts = 0

    while True:
        clearScreen()
        print("Login to InCollege ")
        print("Username: ", end="")
        username = input("")
        print("Password: ", end="")
        password = input("")
        # User input recieved

        # match username and password
        currentUser = userDB.login(username, password)
        if currentUser != None:  # and loginAttempts <= maximum attempts allowed
            # Valid Login
            print("You have successfully logged in")
            # Insert check if they have pending friend request and transfer to that page
            manage_friend_requests(currentUser, userDB)
            # check if they have unread messages and give option to transfer to that page
            if currentUser.hasUnreadMessages():
                print("You have unread messages, would you like to go to inbox? (y/n)")
                while True:
                    userInput = input("")
                    if userInput.lower() == "y":
                        printInbox(currentUser)
                        break
                    elif userInput.lower() == "n":
                        break
                    else:
                        print(invalidInput("y or n"))
            return currentUser
        else:
            # Invalid Login
            print("Incorrect username / password, please try again")
            loginAttempts = loginAttempts + 1

            # TODO: Enforce max login attempts (not required afaik) -noah
            # if loginAttempts >= MAX_LOGIN_ATTEMPTS:
            #     break

            # Allow return
            while True:
                confirm = input("Input c to continue or x to return to menu: ")
                if confirm.upper() == "X":
                    return None
                elif confirm.upper() == "C":
                    break
