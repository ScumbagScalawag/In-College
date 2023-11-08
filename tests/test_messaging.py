import pytest
import json
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.messaging import printMessagingScreen, messagingOptionsList, newMessageOptionsList
from tests.shared import singleUser, test_users_data_message
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


