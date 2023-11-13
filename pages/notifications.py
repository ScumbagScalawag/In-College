from typing import Optional
from common_utils.messages import invalidInput

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from common_utils.utils import clearScreen
from pages.inbox import printInbox
from pages.profiles import createProfile


def printNotificationScreen(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser == None:
        return currentUser

    clearScreen()

    userDB = UserDatabase()
    userDB.loadUsers()

    # incoming friend request notification
    manage_friend_requests(currentUser, userDB)

    # unread message notification
    if currentUser.hasUnreadMessages():
        print("You have unread messages, would you like to go to inbox? (y/n)")
        while True:
            userInput = input("")
            if userInput.lower() == "y":
                printInbox(currentUser)
                break
            elif userInput.lower() == "n":
                break
            else:
                print(invalidInput("y or n"))

    # profile creation notification
    if currentUser.profile.username != currentUser.username:
        print("You have not yet created a profile, would you like to go the profile creation page? (y/n)")
        while True:
            userInput = input("")
            if userInput.lower() == "y":
                currentUser = createProfile(currentUser)
                break
            elif userInput.lower() == "n":
                break
            else:
                print(invalidInput("y or n"))
    
    # new users notifications
    for name in currentUser.unseenUsers:
        print(name, "has joined InCollege")

    return currentUser
