from common_utils.utils import clearScreen, loadUsers, userSearch
import os
import json

# user selected to find someone that you know
def printFriendSearchScreen(currentUserIndex=None):
    users = loadUsers()
    while True:
        clearScreen()
        print("*** Find A Friend ***")
        print("Search for someone you know on InCollege")
        first = input("First name: ")
        last = input("Last name: ")
        # If found, display
        foundUserIndex = userSearch(users, firstname=first, lastname=last)
        if foundUserIndex != False:
            print("They are a part of the InCollege system")
            # If logged in, friend request?
            if currentUserIndex != None:
                confirm = input("Would you like to make a connection with {} {}? (y/n)".format(first, last)).upper()
                while True:
                    if confirm == "Y":
                        addConnection(users, currentUserIndex, foundUserIndex)
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
                return
            elif confirm == "C":
                break

def addConnection(users, currentUserIndex, targetUserIndex):
    users[currentUserIndex]["connections"].append(targetUserIndex)
    users = {"userlist":users}
    os.chdir(os.path.dirname(__file__))
    with open("user_file.json", "w") as outfile:
        json.dump(users, outfile)