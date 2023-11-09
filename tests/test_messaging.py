import pytest
import json
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.messaging import (
    printMessagingScreen,
    messagingOptionsList,
    newMessageOptionsList,
    printNewMessage,
    chooseByName,
)
from tests.shared import singleUser, threeAccountsMessages
from common_utils.messages import invalidInput, anyButtonToContinueMessage


@pytest.mark.parametrize(
    "mock_input,responses",
    [
        (
            ["1"],  # New Message
            [
                *messagingOptionsList,
                *newMessageOptionsList,
            ],
        ),
        (
            ["2"],  # Inbox
            [
                *messagingOptionsList,
                "*** Inbox ***",
            ],
        ),
        (
            ["X"],  # Exit
            [
                *messagingOptionsList,
            ],
        ),
        (
            ["Foam Earplugs"],  # Invalid input
            [
                *messagingOptionsList,
                invalidInput("1, 2, or X"),
            ],
        ),
    ],
)
def testPrintMessagingScreen(mock_input, responses, monkeypatch, capfd):
    inputs = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    testUser = User.dictToUser(singleUser)
    try:
        assert printMessagingScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


def testPrintMessagingScreen_NotLoggedIn(monkeypatch, capfd):
    mock_input = ["Foam Earplugs"]
    inputs = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    testUser = None
    try:
        assert printMessagingScreen(testUser) == testUser
    except StopIteration:
        pass
    responses = [
        "*** InCollege Messaging ***",
        "Messaging is only available for users with accounts",
        anyButtonToContinueMessage(),
    ]

    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


# Adapted from test_send_message_non_plus_to_non_friend
@pytest.mark.parametrize(
    "mock_input,username,responses,messages",
    [
        (
            ["3"],
            "user2",
            [
                *newMessageOptionsList,
                "That feature is only available for InCollege Plus members",
                anyButtonToContinueMessage(),
                # test_send_message_non_plus_to_non_friend
            ],
            [],
        ),
        (
            ["2", "1", "Subject", "Message", "SEND"],
            "user2",
            [
                *newMessageOptionsList,
                "*** New Message ***",
                "Select a friend to message",
                "1 - user3",
                "*** New Message ***",
                "Recipient: user3",
                # test_send_message_non_plus_to_friend
            ],
            ["\nMessage\nSEND"],
        ),
        (
            ["1", "user3", "Subject", "Message", "SEND"],
            "user2",
            [
                *newMessageOptionsList,
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
                "*** New Message ***",
                "Recipient: user3",
                # test_send_message_non_plus_to_friend
            ],
            ["\nMessage\nSEND"],
        ),
        (
            ["X"],
            "user2",
            [
                *newMessageOptionsList,
            ],
            [],
        ),
        (
            ["Foam Earplugs"],
            "user2",
            [
                *newMessageOptionsList,
                invalidInput("1, 2, 3, or X"),
                anyButtonToContinueMessage(),
            ],
            [],
        ),
    ],
    ids=[
        "3-Non-plus user",
        "2-Non-plus user to friend by friends",
        "1-Non-plus user to friend by name",
        "X-Exit",
        "Invalid input",
    ],
)
def testPrintNewMessage(mock_input, username, responses, messages, monkeypatch, capfd):
    user_db = UserDatabase()
    user_db.addUserDictList(threeAccountsMessages)
    user_db.saveDatabase()
    testUser = user_db.getUser(username)  # A non-plus user
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printNewMessage(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    user_db.loadUsers()
    if messages != []:
        recipient_data = User.toDict(user_db.getUser("user3"))  # scuffed
        last_message = recipient_data["incomingMessages"][1]
        assert last_message["subject"] == "Subject"
        assert last_message["message"] == messages[0]


@pytest.mark.parametrize(
    "mock_input,username,responses,expected_return",
    [
        (
            ["user3"],
            "user2",
            [
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
            ],
            "user3",
        ),
        (
            ["X"],
            "user2",
            [
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
            ],
            None,
        ),
        (
            ["Foam Earplugs"],
            "user2",
            [
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
                "User is not in the InCollege system",
                anyButtonToContinueMessage(),
            ],
            None,
        ),
        (
            ["user1"],
            "user2",
            [
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
                "I'm sorry, you are not friends with that person",
                anyButtonToContinueMessage(),
            ],
            None,
        ),
        (
            ["user2"],
            "user1",
            [
                "*** New Message ***",
                "Enter username of user you would like to message, or X to return to previous menu",
            ],
            "user2",
        ),
    ],
    ids=["Valid input", "X-Exit", "Invalid input", "Not friends", "Plus User"],
)
def testChooseByName(mock_input, username, responses, expected_return, monkeypatch, capfd):
    user_db = UserDatabase()
    user_db.addUserDictList(threeAccountsMessages)
    user_db.saveDatabase()
    testUser = user_db.getUser(username)  # A non-plus user
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert chooseByName(testUser) == expected_return
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


def testChooseFromFriends(monkeypatch, capfd):
    pass
