from typing import Optional
from common_utils.messages import mustBeLoggedIn, returnToPreviousMenuMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printGuestControlsPage(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()

    # make sure DB/Json is updated too
    userDB = UserDatabase([])
    userDB.loadUsers()

    if currentUser is None:
        print("You must be logged in to access guest controls.\n")
        return currentUser

    while True:
        printOptionList(guestControlsList)
        userInput = input("")

        if userInput == "1":
            currentUser = toggleUserEmailSubscription(currentUser)
            # make sure DB/Json is updated too
            userDB.updateUser(currentUser)
            continue
        elif userInput == "2":
            currentUser = toggleUserSmsSubscription(currentUser)
            userDB.updateUser(currentUser)
            continue
        elif userInput == "3":
            currentUser = toggleUserTargetedAds(currentUser)
            userDB.updateUser(currentUser)
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

notificationSettingsError = "ERROR: there was a problem with changing notification settings "
unsubscribeMessage = "You have successfully unsubscribed from InCollege "
subscribeMessage = "You have successfully subscribed to InCollege "


def toggleUserEmailSubscription(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser == None:
        print(mustBeLoggedIn())
        return currentUser

    originalBool = currentUser.emailSub
    currentUser.toggleEmailSub()
    toggleCheck(currentUser.emailSub, originalBool, "emails")

    return currentUser


def toggleUserSmsSubscription(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser == None:
        print(mustBeLoggedIn())
        return currentUser

    originalBool = currentUser.smsSub
    currentUser.toggleSmsSub()
    toggleCheck(currentUser.smsSub, originalBool, "SMS Messages")

    return currentUser


def toggleUserTargetedAds(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser == None:
        print(mustBeLoggedIn())
        return currentUser

    originalBool = currentUser.adSub
    currentUser.toggleAdSub()
    toggleCheck(currentUser.adSub, originalBool, "Targeted Advertizing")

    return currentUser


def toggleCheck(currentUserBool, originalBool, toggleType):
    if originalBool == True:
        if currentUserBool == True:
            print(notificationSettingsError, 2)
        print(unsubscribeMessage, toggleType)
    elif originalBool == False:
        if currentUserBool == False:
            print(notificationSettingsError, 3)
        print(subscribeMessage, toggleType)
    else:
        raise Exception(notificationSettingsError, 1)
