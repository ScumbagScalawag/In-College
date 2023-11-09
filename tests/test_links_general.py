import pytest
from common_utils.messages import anyButtonToContinueMessage, invalidInput
from pages.links_general import (
    printGeneralScreen,
    generalOptionsList,
    helpOptions,
    aboutOptions,
    pressOptions,
    blogOptions,
    careersOptions,
    developersOptions,
)
from tests.shared import singleUser, fourAccounts
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # Help Center
            [
                *generalOptionsList,
                *helpOptions,
            ],
            None,
        ),
        (
            ["2"],  # About
            [
                *generalOptionsList,
                *aboutOptions,
            ],
            None,
        ),
        (
            ["3"],  # Press
            [
                *generalOptionsList,
                *pressOptions,
            ],
            None,
        ),
        (
            ["4"],  # Blog
            [
                *generalOptionsList,
                *blogOptions,
            ],
            None,
        ),
        (
            ["5"],  # Careers
            [
                *generalOptionsList,
                *careersOptions,
            ],
            None,
        ),
        (
            ["6"],  # Developers
            [
                *generalOptionsList,
                *developersOptions,
            ],
            None,
        ),
        (
            ["7"],  # Sign up
            [
                *generalOptionsList,
                "*** Create a new user account ***",
            ],
            None,
        ),
        (
            ["x"],  # Exit
            [
                *generalOptionsList,
            ],
            None,
        ),
        (
            ["Foam Earplugs"],  # Invalid Input
            [
                *generalOptionsList,
                invalidInput("1, 2, 3, 4, 5, 6, 7 or X"),
                anyButtonToContinueMessage(),
            ],
            None,
        ),
    ],
    ids=[
        "1-Help Center",
        "2-About",
        "3-Press",
        "4-Blog",
        "5-Careers",
        "6-Developers",
        "7-Sign up",
        "X-Exit",
        "Invalid Input",
    ],
)
def testPrintGeneralScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printGeneralScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


# Test to see if option 7 shows up if logged in
# Expected to fail until general screen is fixed.
def testPrintGeneralSignUpNotShown(monkeypatch, capfd):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)

    mock_input = ["anything"]
    responses = [
        *generalOptionsList,
    ]
    responses_missing = [
        "7 - Sign up",
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printGeneralScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    for r in responses_missing:
        assert r not in captured.out
