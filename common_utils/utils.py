import json
import os

JSON_USERS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")
JSON_JOBS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobs.json")
from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User

MAX_USERS = 10
MAX_JOBS = 10


# Use this for making options lists in pages
def printOptionList(options):
    for option in options:
        print(option)


# Works on Windows and Unix
def clearScreen():
    # Check the operating system and use the appropriate clear command
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")
    else:
        print("Unsupported operating system: Cannot clear the screen.")


def pathToUserFile(relativePath, dataBaseName):
    # return os.path.join(os.path.dirname(os.path.abspath(__file__)), relativePath, dataBaseName)
    calling_file_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(calling_file_directory, relativePath, dataBaseName)
    return full_path


# NOTE: returns user so we don't need a global user -noah
def loadUsers():
    users = []
    try:
        with open(pathToUserFile("..", "user_file.json"), "r") as database:
            users = json.load(database)
            users = users["userlist"]
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
        print(
            "WARNING: Cannot find JSON DataBase!"
        )  # feel free to comment this message out. I find it helpful -noah
        pass

    return users


# should use JobDatabase.loadJobs() instead
# def loadJobs():
#     jobs = []
#     try:
#         with open(JSON_JOBS_FP, "r") as database:
#             jobs = json.load(database)
#             jobs = jobs["joblist"]
#     except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
#         print(
#             "WARNING: Cannot find JSON DataBase!"
#         )  # feel free to comment this message out. I find it helpful -noah
#         pass

#     return jobs


def userSearch(
    users,
    username=None,
    password=None,
    firstname=None,
    lastname=None,
    returnUsername=False,
    returnUserObject=False,
):
    # serves as a flag that a previous requirement was used
    # also ensures that it doesn't get false positive for cases like a different user's password for example
    foundUserIndex = None

    # check if username is incorrect
    if username != None:
        for i, user in enumerate(users):
            if user["username"] == username:
                foundUserIndex = i
                break
        if foundUserIndex == None:
            return False

    # check if password is correct
    if password != None:
        if foundUserIndex != None:
            if users[foundUserIndex]["password"] != password:
                return False
        else:
            for i, user in enumerate(users):
                if user["password"] == password:
                    foundUserIndex = i
                    break
            if foundUserIndex == None:
                return False

    # check if firstname is incorrect
    if firstname != None:
        if foundUserIndex != None:
            if users[foundUserIndex]["firstname"] != firstname:
                return False
        else:
            for i, user in enumerate(users):
                if user["firstname"] == firstname:
                    foundUserIndex = i
                    break
            if foundUserIndex == None:
                return False

    # check if lastname is incorrect
    if lastname != None:
        if foundUserIndex != None:
            if users[foundUserIndex]["lastname"] != lastname:
                return False
        else:
            for i, user in enumerate(users):
                if user["lastname"] == lastname:
                    foundUserIndex = i
            if foundUserIndex == None:
                return False

    # case for if we want to know the username, not just whether it exists
    if returnUsername:
        return users[foundUserIndex]["username"]

    # case for if we want to return the entire user Object
    if returnUserObject:
        return users[foundUserIndex]

    # if nothing that was searched for is incorrect, it all must have been found
    return True


# check if currentUser is logged in
def notLoggedIn(currentUser):
    if not isinstance(currentUser, User):
        print("You must be logged in to view this page.")
        return True
    else:
        return False
