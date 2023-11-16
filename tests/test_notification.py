from datetime import date, datetime
from typing import Optional

import pytest  # needed for pytest

from common_utils.messages import invalidInput
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from common_utils.utils import anyButtonToContinueMessage, clearScreen
from pages.inbox import printInbox
from pages.profiles import createProfile
from tests.shared import JSON_USERS_FP, fourAccounts  # needed for testWithDatabaseSet


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

    # new users notifications
    flag = 0
    for name in currentUser.unseenUsers:
        flag = 1
        print(name, "has joined InCollege")
        # remove name from unseenUsers
    if flag:
        print(anyButtonToContinueMessage())
        input("")

    return currentUser


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["", ""],  # mock input
            [
                "",  # responses
                "",
            ],
            None,  # expected return
        ),
        (
            ["1st input", "2nd input"],
            [
                "",
                "",
            ],
            None,
        ),
        (
            [""],
            [
                "",
            ],
            None,
        ),
    ],
)
def testTempName(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printNotificationScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
