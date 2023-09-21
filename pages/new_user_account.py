from common_utils.utils import clearScreen, loadUsers, userSearch
from pages.main_menu import printMainMenu
import os
import json

MAXUSERS = 5
JSONFP = os.path.join(os.path.dirname(__file__), '..')


# Menu: Add new user account
def printNewAccountScreen():
    users = loadUsers()

    if len(users) < MAXUSERS:  # Requirement for 5 accounts
        while True:
            clearScreen()
            print("*** Create a new user account ***")
            username = input("Username: ")  # Get username
            # check that username is not already in use
            if not userSearch(users, username=username):
                firstname = input("First name: ")
                lastname = input("Last name: ")
                password = input("Password: ")  # Get password
                if checkPasswordSecurity(password):  # Is password secure
                    passwordConfirm = input("Confirm password: ")  # Get password confirmation
                    if password == passwordConfirm:  # Confirm passwords
                        saveUser(users, username, password, firstname, lastname)  # Add new account
                        currentUser = userSearch(users, username=username, returnUsername=True) # get logged in user
                        printMainMenu(currentUser)
                        return 0
                    else:
                        print("Passwords do not match")
                else:
                    print(
                        "Password Requirements: minimum of 8 characters, maximum of 12 characters"
                        "at least 1 capital letter, at least 1 digit, at least 1 special character"
                    )
            else:
                print("This username is already in use.")  # wordage taken from roblox.com
            
            # Allow return
            while True:
                confirm = input("Input c to continue or x to return to menu: ").upper()
                if confirm == "X":
                    return 0
                elif confirm == "C":
                    break
    print("All permitted accounts have been created, come back later")  # Requirement for 5 accounts response
    print("Please press any button to continue")
    userInput = input()
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

# Helper: Save username and password to user dictionary and to JSON
def saveUser(users, username, password, firstname, lastname):
    newUser = {"username":username,
               "password":password,
               "firstname":firstname,
               "lastname":lastname,
               "connections":[]}
    users.append(newUser)
    users = {"userlist":users}
    os.chdir(JSONFP)
    with open("user_file.json", "w") as outfile:
        json.dump(users, outfile, indent=4)
