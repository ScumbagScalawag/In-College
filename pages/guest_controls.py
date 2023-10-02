from typing import Optional
from common_utils.messages import invalidInput, mustBeLoggedIn, returnToPreviousMenuMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


def printGuestControlsPage(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()

    if currentUser is None:
        print("You must be logged in to access guest controls.\n")
        return currentUser

    while True:
        clearScreen()

        # Title & Input Options
        printOptionList(guestControlsList)
        print("\n")

        # Let users know if they are subscribed or not
        if isinstance(currentUser, User):
            sms = "Subscribed" if currentUser.smsSub == True else "Unsubscribed"
            email = "Subscribed" if currentUser.emailSub == True else "Unsubscribed"
            ads = "Subscribed" if currentUser.adSub == True else "Unsubscribed"
        else:
            sms = "UNKNOWN"
            email = "UNKNOWN"
            ads = "UNKNOWN"
        guestSettings = [
            "Current Guest Control Settings",
            f"InCollege Email Subscription: {email}",
            f"InCollege SMS Subscription: {sms}",
            f"InCollege Targeted Advertizing: {ads}",
        ]
        printOptionList(guestSettings)
        userInput = input("")

        # Take input
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
            print(invalidInput('"1" or "2" or "3" or "X"'))

    return currentUser


guestControlsList = [
    "*** Guest Controls ***",
    "1 - Toggle InCollege Email Subscription Status",
    "2 - Toggle SMS Subscription Status",
    "3 - Toggle Targeted Advertizing Features",
    returnToPreviousMenuMessage(),
]

notificationSettingsError = "ERROR: there was a problem with changing notification settings"
unsubscribeMessage = "You have successfully unsubscribed from InCollege"
subscribeMessage = "You have successfully subscribed to InCollege"


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


# Toggle User boolean values
def toggleCheck(currentUserBool: bool, originalBool: bool, toggleType: str):
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
