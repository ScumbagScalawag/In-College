from common_utils.utils import clearScreen, loadUsers, userSearch, JSON_USERS_FP, printOptionList
import json


# user selected to find someone that you know
def printFriendSearchScreen(currentUser=None):
    users = loadUsers()
    while True:
        clearScreen()
        printOptionList(friendSearchOptionList)
        first = input("First name: ")
        last = input("Last name: ")

        # check for multiple users
        foundUserList = []
        foundUser = None
        while True:
            foundUser = userSearch(users, firstname=first, lastname=last, returnUsername=True, excludeList=foundUserList)
            if foundUser != False:
                foundUserList.append(foundUser)
            else:
                break

        # if multiple users found, ask which username
        # cancellation flag
        flag = 0
        if len(foundUserList) > 1:
            print("Found multiple users with that name")
            print("Which are you looking for?")
            while True:
                for i, user in enumerate(foundUserList):
                    optionNum = i + 1
                    print(optionNum, "-", user)
                print("X - None of the above")
                notInt = 0
                userInput = input("")

                # check if it is X, or make it an int
                if userInput.upper() == "X":
                    flag = 1
                    break
                else:
                    try:
                        userInput = int(userInput)
                    except:
                        notInt = 1

                # not an int
                if notInt:
                    pass
                # not an option
                elif userInput < 1 or userInput > len(foundUserList):
                    pass
                # otherwise, select option
                else:
                    i = userInput - 1
                    foundUser = foundUserList[i]
                    break
                # print message before reiterating options
                print("Invalid input, select one of the following options:")

        # if only one user in list, use that one
        elif len(foundUserList) == 1:
            foundUser = foundUserList[0]

        # skip making connection if user not found or not selected from list
        if flag:
            pass
        elif foundUser == False:
            print("They are not yet a part of the InCollege system yet")
        # If found, display
        else:
            print("They are a part of the InCollege system")
            # If logged in, friend request?
            if currentUser != None:
                confirm = input(
                    "Would you like to make a connection with {} {}? (y/n)".format(first, last)
                ).upper()
                while True:
                    if confirm == "Y":
                        msg = addConnection(users, currentUser, foundUser)
                        print(msg)
                        break
                    elif confirm == "N":
                        break
                    else:
                        confirm = input("Please input y or n: ").upper()
            else:
                return -1
        # If not found, display
        

        # Allow return
        while True:
            confirm = input("Input c to continue or x to return to menu: ").upper()
            if confirm == "X":
                return 0
            elif confirm == "C":
                break


friendSearchOptionList = [
    "*** Find A Friend ***",
    "Search for someone you know on InCollege",
]


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
