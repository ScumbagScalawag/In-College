from datetime import date, datetime
from typing import Optional

from common_utils.messages import invalidInput
from common_utils.types.job_database import JobDatabase
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from common_utils.utils import anyButtonToContinueMessage, clearScreen
from pages.inbox import printInbox
from pages.profiles import createProfile


def printNotificationScreen(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser == None:
        return currentUser

    clearScreen()

    userDB = UserDatabase()
    userDB.loadUsers()

    # apply to more jobs notification
    flag = 0
    if currentUser.lastApplicationDate == "UNDEFINED":
        flag = 1
    else:
        splitDate = currentUser.lastApplicationDate.split("-")
        lastApplication = date((int)(splitDate[0]), (int)(splitDate[1]), (int)(splitDate[2]))
        timeDifference = date.today() - lastApplication
        if timeDifference.days > 7:
            flag = 1
    if flag:
        print(
            "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!"
        )
        print(anyButtonToContinueMessage())
        input("")

    # incoming friend request notification
    manage_friend_requests(currentUser, userDB)

    print("")

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

    print("")

    currentUser = deletedJobNotification(currentUser)

    print("")

    # profile creation notification
    if currentUser.profile.username != currentUser.username:
        print(
            "You have not yet created a profile, would you like to go the profile creation page? (y/n)"
        )
        while True:
            userInput = input("")
            if userInput.lower() == "y":
                currentUser = createProfile(currentUser)
                break
            elif userInput.lower() == "n":
                break
            else:
                print(invalidInput("y or n"))

    print("")

    # new job has been posted notification
    newJobCreationNotification(currentUser.username)

    print("")

    # new users notifications
    flag = 0
    for name in currentUser.unseenUsers:
        flag = 1
        print(name, "has joined InCollege")
        currentUser.removeUnseen(name)
    userDB.saveDatabase()
    if flag:
        print(anyButtonToContinueMessage())
        input("")

    return currentUser


def deletedJobNotification(currentUser: Optional[User] = None) -> Optional[User]:
    if currentUser != None and currentUser.applicationDeleted != "UNDEFINED":
        print(f"A job that you applied for has been deleted ({currentUser.applicationDeleted})")


def newJobCreationNotification(username):
    jobDB = JobDatabase()
    jobDB.loadJobs()
    foundJobTitles = []

    for job in jobDB.joblist:
        if username not in job.seenBy:
            foundJobTitles.append(job.title)
            job.seenBy.append(username)
            jobDB.saveDatabase()

    if len(foundJobTitles) == 0:
        return

    for i in range(0, len(foundJobTitles)):
        print(f"A new job {foundJobTitles[i]} has been posted")

    return
