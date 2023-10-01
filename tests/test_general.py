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
from pages.new_user_account import saveDatabase


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
def testPrintGeneralSignUp(monkeypatch, capfd):
    saveDatabase(JSON_USERS_FP, threeAccounts)
    mock_input = [
        "7",
        singleUser["username"],
        singleUser["firstname"],
        singleUser["lastname"],
        singleUser["password"],
        singleUser["password"],
    ]
    responses = [
        *generalOptionsList,
        "*** Create a new user account ***",
    ]
    expectedReturn = singleUser["username"]
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
def testPrintGeneralSignUpNotShown(monkeypatch, capfd):
    saveDatabase(JSON_USERS_FP, fourAccounts)  # not needed but just incase
    mock_input = ["anything"]
    responses = [
        *generalOptionsList,
    ]
    responses_missing = [
        "7 - Sign up",
    ]
    expectedReturn = singleUser["username"]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printGeneralScreen(singleUser["username"]) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    for r in responses_missing:
        assert r not in captured.out