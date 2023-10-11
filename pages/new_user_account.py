from typing import Optional
from common_utils.types.exceptions import MaximumNumberOfUsers
from common_utils.utils import clearScreen, MAX_USERS
from common_utils.messages import alreadyLoggedIn, anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase


# Menu: Add new user account
def printNewAccountScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # users = loadUsers()
    userDB = UserDatabase()
    userDB.loadUsers()

    if isinstance(currentUser, User):
        print(alreadyLoggedIn("Please log out to create another account."))
        return currentUser

    if len(userDB.userlist) < MAX_USERS:  # Requirement for 5 accounts
        while True:
            clearScreen()
            print("*** Create a new user account ***")
            print("Username: ", end="")
            username = input("")  # Get username
            # check that username is not already in use
            # if not userSearch(users, username=username):
            if not userDB.userExists(username):
                print(
                    "First name: ", end=""
                )  # Changed from input("...") to print("...", end="") for testing
                firstname = input("")
                print("Last name: ", end="")
                lastname = input("")
                print("University: ", end="")
                uni = input("")
                print("Major: ", end="")
                major = input("")
                print("Password: ", end="")
                password = input("")  # Get password
                if checkPasswordSecurity(password):  # Is password secure
                    passwordConfirm = input("Confirm password: ")  # Get password confirmation
                    if password == passwordConfirm:  # Confirm passwords
                        newUser = User(
                            username,
                            password,
                            firstname,
                            lastname,
                            uni,
                            major,
                        )
                        # Just in case. Conditional check beforehand should catch this
                        try:
                            userDB.addUser(newUser)
                        except ( MaximumNumberOfUsers) as e:  
                            print(f"Error: {e}")
                            print(anyButtonToContinueMessage())
                            input("")
                            break

                        # check if user made it to DB
                        if userDB.userExists(username):
                            # either returns user or False
                            currentUser = userDB.getUser(username)
                            if currentUser == False:
                                currentUser = None  # must return None | User for context
                            return currentUser
                        else:
                            print(
                                "There was an unexpected problem with adding new account. Please try again."
                            )
                    else:
                        print("Passwords do not match")
                else:
                    print(
                        "Password Requirements: minimum of 8 characters, maximum of 12 characters, "
                        "at least 1 capital letter, at least 1 digit, at least 1 special character"
                    )
            else:
                print("This username is already in use.")  # wordage taken from roblox.com

            # Allow return
            while True:
                confirm = input("Input c to continue or x to return to menu: ").upper()
                if confirm == "X":
                    return None
                elif confirm == "C":
                    break
    else:
        print(
            "All permitted accounts have been created, come back later"
        )  # Requirement for 5 accounts response
        print(anyButtonToContinueMessage())
        input("")
    return None


# Helper: Password strength criteria check
def checkPasswordSecurity(password):
    capitalFlag = 0  # At least 1 capital letter
    digitFlag = 0  # At least 1 digit
    specialFlag = 0  # At least 1 special character
    pLen = len(password)  # might need to change name of variable
    if pLen < 8 or pLen > 12:  # Minimum 8 characters - Maximum 12 Characters
        return False  # Password is either too short or too long

    for char in password:
        if char.isnumeric():  # is a digit
            digitFlag = 1
        if char.isupper():  # is uppercase
            capitalFlag = 1
        if char.isascii() and not char.isalnum():  # is ascii but not alpha-numerical
            specialFlag = 1

    if capitalFlag and digitFlag and specialFlag:
        return True  # Password is valid

    return False  # Password is invalid
