from typing import Optional
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, loadUsers, userSearch, JSON_USERS_FP, printOptionList
import json


# user selected to find someone that you know
def printFriendSearchScreen(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()

    while True:
        clearScreen()
        printOptionList(friendSearchOptionList)
        first = input("First name: ")
        last = input("Last name: ")
        # If found, display
        foundUser = userDB.userSearch(firstname=first, lastname=last)

        if foundUser != None:
            print("They are a part of the InCollege system")

            print(type(currentUser))
            print(currentUser)
            print("\n")
            # If logged in, friend request?
            if currentUser != None:
                confirm = input(
                    "Would you like to make a connection with {} {}? (y/n)".format(first, last)
                ).upper()
                while True:
                    if confirm == "Y":
                        if currentUser.isConnection(foundUser.username):
                            print("You are already connected with this user")
                            break
                        elif currentUser == foundUser:
                            print("You cannot make a connection with yourself")
                            break
                        # Testing Stuff:

                        # foundUser
                        print("foundUser Type: ", type(currentUser))
                        print("foundUser: ", foundUser)
                        print("foundUser.username = ", foundUser.username)
                        print("userDB: ", userDB)

                        addConnectionValue = currentUser.addConnection(foundUser.username)
                        if addConnectionValue != 0:
                            print(
                                f"There was an error adding connection. Code {addConnectionValue}"
                            )

                        print("currentUser before updating DB: ", currentUser)
                        print("DB before updating DB: ", userDB)
                        updateDBReturn = userDB.updateUser(currentUser)  # NOT WORKING
                        if updateDBReturn == False:
                            print("updateUser() has failed")

                        # userDB.saveDatabase()
                        print("userDB (After being Updated): ", userDB)  # NOT WORKING

                        #testing DB was written to Json File correctly 
                        loadDB = UserDatabase([])
                        loadDB.loadUsers()
                        print("loadDB: Testing that Json was written to: ", loadDB)
                        # Testing Stuff ^

                        print("Connection request sent")
                        break
                    elif confirm == "N":
                        break
                    else:
                        confirm = input("Please input y or n: ").upper()
            else:
                return currentUser
        # If not found, display
        else:
            print("They are not yet a part of the InCollege system yet")

        # Allow return
        while True:
            confirm = input("Input c to continue or x to return to menu: ").upper()
            if confirm == "X":
                return currentUser
            elif confirm == "C":
                break


friendSearchOptionList = [
    "*** Find A Friend ***",
    "Search for someone you know on InCollege",
]


# Depreciated by User.addConnection()
def addConnection(users, currentUser, targetUser):
    currentUserIndex = None
    # doesn't let you add yourself
    if currentUser == targetUser:
        msg = "You cannot make a connection with yourself"
        return msg
    # get index of current user
    for i, user in enumerate(users):
        if user["username"] == currentUser:
            currentUserIndex = i
            break
    # doesn't let you add someone you already added
    if targetUser in users[currentUserIndex]["connections"]:
        msg = "You are already connected with this user"
        return msg
    # adds target to connections list and updates file
    users[currentUserIndex]["connections"].append(targetUser)
    users = {"userlist": users}
    with open(JSON_USERS_FP, "w") as outfile:
        json.dump(users, outfile, indent=4)
    msg = "Connection request sent"
    return msg
