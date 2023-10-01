from common_utils.messages import returnToPreviousMenuMessage
from common_utils.utils import clearScreen, loadUsers, printOptionList, userSearch


def printGuestControlsPage(currentUser=None):
    clearScreen()

    if currentUser == None:
        print("You must be logged in to access guest controls.")
        return currentUser

    while True:
        printOptionList(guestControlsList)
        userInput = input("")

        if userInput == "1":
            continue
        elif userInput == "2":
            continue
        elif userInput == "3":
            continue
        elif userInput.upper() == "X":
            break
        else:
            print('Invalid selection please input "1" or "2" or "3" or "X"')
    return currentUser


guestControlsList = [
    "*** Guest Controls ***",
    "1 - InCollege Email Subscription",
    "2 - SMS Subscription",
    "3 - Targeted Advertizing Features",
    returnToPreviousMenuMessage(),
]


def toggleUserEmailSubscription(currentUser=None):
    # userName = userSearch(loadUsers(), returnUsername=True)
    if currentUser != None:
        userObject = userSearch(loadUsers(), username=currentUser, returnUserObject=True)
        # userObject["emailSub"]
        return True

    return False
