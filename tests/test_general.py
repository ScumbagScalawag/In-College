import pytest
from pages.links_general import (
    printGeneralScreen,
    generalOptionsList,
    aboutOptions,
    pressOptions,
    blogOptions,
    careersOptions,
    developersOptions,
    helpOptions,
)
from tests.shared import threeAccounts, singleUser, fourAccounts, JSON_USERS_FP

# from pages.new_user_account import saveDatabase
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase


# TODO Rename this file when general gets its own .py file name
@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # HelpCenter
            [*generalOptionsList, *helpOptions],
            [],
        ),
        (
            ["2"],  # About
            [*generalOptionsList, *aboutOptions],
            [],
        ),
        (
            ["3"],  # Press
            [*generalOptionsList, *pressOptions],
            [],
        ),
        (
            ["4"],  # Blog
            [*generalOptionsList, *blogOptions],
            [],
        ),
        (
            ["5"],  # Careers
            [*generalOptionsList, *careersOptions],
            [],
        ),
        (
            ["6"],  # Developers
            [*generalOptionsList, *developersOptions],
            [],
        ),
        (
            ["X"],  # Return
            [
                *generalOptionsList,
            ],
            None,  # We are currentUser=None
        ),
        (
            ["FoamEarplugs"],  # Invalid Input
            [
                *generalOptionsList,
                # TODO: Invalid input not handled
            ],
            [],
        ),
    ],
    ids=[
        "1-HelpCenter",
        "2-About",
        "3-Press",
        "4-Blog",
        "5-Careers",
        "6-Developers",
        "X-Return",
        "TODO: InvalidSelection",
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

    # TODO Test Option 7 Logged in
    userDB = UserDatabase([])
    userDB.addUserDictList(threeAccounts)
    testUser = User.dictToUser(singleUser)
    mock_input = [
        "7",
        testUser.username,
        testUser.firstname,
        testUser.lastname,
        testUser.password,
        testUser.password,
    ]
    responses = [
        *generalOptionsList,
        "*** Create a new user account ***",
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printGeneralScreen() == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


# Test to see if option 7 shows up if logged in
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
