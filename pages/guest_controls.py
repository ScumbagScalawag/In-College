from common_utils.messages import returnToPreviousMenuMessage
from common_utils.utils import clearScreen, printOptionList


def printGuestControlsPage():
    clearScreen()
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
    return


guestControlsList = [
    "*** Guest Controls ***",
    "1 - InCollege Email Subscription",
    "2 - SMS Subscription",
    "3 - Targeted Advertizing Features",
    returnToPreviousMenuMessage()
]
