from common_utils.utils import clearScreen, loadUsers
from pages.main_menu import printMainMenu
import os
import json

MAXUSERS = 5


# Menu: Add new user account
def printNewAccountScreen():
    clearScreen()
    
    user = loadUsers()

    login = False
    if getNumUsers(user) < MAXUSERS:  # Requirement for 5 accounts
        while True:
            print("*** Create a new user account ***")
            print("Username: ", end="")
            username = input()  # Get username
            if isUniqueUser(user, username):
                print("Password: ", end="")
                password = input()  # Get password
                if checkPasswordSecurity(password):  # Is password secure
                    print("Confirm password: ", end="")
                    passwordConfirm = input()  # Get password confirmation
                    if password == passwordConfirm:  # Confirm passwords
                        saveUser(user, username, password)  # Add new account
                        login = True
                        break
                    else:
                        print("Passwords do not match")
                else:
                    print(
                        "Password Requirements: minimum of 8 characters, maximum of 12 characters"
                        "at least 1 capital letter, at least 1 digit, at least 1 special character"
                    )
            else:
                print("This username is already in use.")  # wordage taken from roblox.com
        if login:
            printMainMenu()
            return 0 # successfully returns -> user logged in, went to main menu, printMainMenu() returns (user exited or something)
        # Implicity catches the case where User is somehow not logged in yet 
        return -1
    # Implicity catches the case where MAXUSERS > 5; ensures funct always returns -noah
    print("All permitted accounts have been created, and come back later")  # Requirement for 5 accounts response
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


# Helper: Used in login to return the number of users
def getNumUsers(user):
    return len(user)


# Helper: Unique username check
def isUniqueUser(user, username):
    for i in user:
        if i == username:
            return False  # Username found
    return True  # Username not found, is unique


# Helper: Save username and password to user dictionary and to JSON
def saveUser(user, username, password):
    user[username] = password
    os.chdir(os.path.dirname(__file__))
    with open("user_file.json", "w") as outfile:
        json.dump(user, outfile)
