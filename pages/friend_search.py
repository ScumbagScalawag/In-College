from common_utils.utils import clearScreen, loadUsers, userSearch
import os
import json

JSONFP = os.path.join(os.path.dirname(__file__), '..')

# user selected to find someone that you know
def printFriendSearchScreen(currentUser=None):
    users = loadUsers()
    while True:
        clearScreen()
        print("*** Find A Friend ***")
        print("Search for someone you know on InCollege")
        first = input("First name: ")
        last = input("Last name: ")
        # If found, display
        foundUser = userSearch(users, firstname=first, lastname=last, returnUsername=True)
        if foundUser != False:
            print("They are a part of the InCollege system")
            # If logged in, friend request?
            if currentUser != None:
                confirm = input("Would you like to make a connection with {} {}? (y/n)".format(first, last)).upper()
                while True:
                    if confirm == "Y":
                        addConnection(users, currentUser, foundUser)
                    elif confirm == "N":
                        break
                    else:
                        confirm = input("Please input y or n: ").upper()
        # If not found, display
        else:
            print("They are not yet a part of the InCollege system yet")    

        # Allow return
        while True:
            confirm = input("Input c to continue or x to return to menu: ").upper()
            if confirm == "X":
                return 0
            elif confirm == "C":
                break

def addConnection(users, currentUser, targetUser):
    # get index of current user
    for i, user in enumerate(users):
        if user["username"] == currentUser:
            currentUserIndex = i
            break
    # find current user's connection list and append target user
    users[currentUserIndex]["connections"].append(targetUser)
    users = {"userlist":users}
    os.chdir(JSONFP)
    with open("user_file.json", "w") as outfile:
        json.dump(users, outfile, indent=4)