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


# TODO: probably needs to be loadUsers(user): so we don't have to have a global variable
# should also return the "user" dict
def loadUsers():
    user = {}
    try:
        os.chdir(os.path.dirname(__file__))
        with open("user_file.json", "r") as database:
            user = json.load(database)
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
        print("WARNING: There is no JSON DataBase!")  # feel free to comment this message out. I find it helpful -noah
        pass

    return user
