import os
import json


# Works on Windows and Unix
def clearScreen():
    # Check the operating system and use the appropriate clear command
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")
    else:
        print("Unsupported operating system: Cannot clear the screen.")


# NOTE: returns user so we don't need a global user -noah
def loadUsers():
    users = []
    try:
        os.chdir(os.path.dirname(__file__))
        with open("user_file.json", "r") as database:
            users = json.load(database)["userlist"]
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
        print("WARNING: Cannot find JSON DataBase!")  # feel free to comment this message out. I find it helpful -noah
        pass

    return users

def userSearch(users, username=None, password=None, firstname=None, lastname=None, returnIndex=False):
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
    if returnIndex:
        return foundUserIndex

    # if nothing that was searched for is incorrect, it all must have been found
    return True
    