from typing import List
from common_utils.utils import clearScreen, loadUsers, userSearch, JSON_USERS_FP
from common_utils.messages import anyButtonToContinueMessage
import json

MAXUSERS = 5


# Menu: Add new user account
def printNewAccountScreen():
    users = loadUsers()

    if len(users) < MAXUSERS:  # Requirement for 5 accounts
        while True:
            clearScreen()
            print("*** Create a new user account ***")
            print("Username: ", end="")
            username = input("")  # Get username
            # check that username is not already in use
            if not userSearch(users, username=username):
                print(
                    "First name: ", end=""
                )  # Changed from input("...") to print("...", end="") for testing
                firstname = input("")
                print("Last name: ", end="")
                lastname = input("")
                print("Password: ", end="")
                password = input("")  # Get password
                if checkPasswordSecurity(password):  # Is password secure
                    passwordConfirm = input("Confirm password: ")  # Get password confirmation
                    if password == passwordConfirm:  # Confirm passwords
                        saveUser(
                            users,
                            username,
                            password,
                            firstname,
                            lastname,
                        )  # Add new account
                        currentUser = userSearch(
                            users, username=username, returnUsername=True
                        )  # get logged in user
                        return currentUser
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
        userInput = input("")
    return -1


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


# users takes the list, not the entire dict!
def saveUser(
    users: List,
    username: str = "UNDEFINED",
    password: str = "UNDEFINED",
    firstname: str = "UNDEFINED",
    lastname: str = "UNDEFINED",
    email: str = "UNDEFINED",
    phoneNumber: str = "UNDEFINED",
    emailSub: bool = True,
    smsSub: bool = True,
    adSub: bool = True,
    connections: List = []
):
    newUser = {
        "username": username,
        "password": password,
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "phoneNumber": phoneNumber,
        "emailSub": emailSub,
        "smsSub": smsSub,
        "adSub": adSub,
        "connections": connections
    }
    users.append(newUser)
    saveDatabase(JSON_USERS_FP, users)


# users takes the list, not the entire dict!
def saveDatabase(jsonFilePath, users):
    userDB = {"userlist": users}
    with open(jsonFilePath, "w") as outfile:
        json.dump(userDB, outfile, indent=4)
