import pytest

import json
from common_utils.utils import loadUsers
from pages.new_user_account import printNewAccountScreen, saveDatabase, saveUser
from tests.shared import JSON_USERS_FP, singleUser, threeAccounts, fiveAccounts


@pytest.mark.parametrize(
    "mock_input,responses,startingUserDB,numUsers,expectedReturn",
    [
        (
            ["user6", "Jesse", "Small", "P@ssword1", "P@ssword1", "anything"],
            [
                "All permitted accounts have been created, come back later",
                "Please press any button to continue",
            ],
            fiveAccounts,
            5,
            -1,
        ),
        (
            [
                singleUser[0]["username"],
                singleUser[0]["firstname"],
                singleUser[0]["lastname"],
                singleUser[0]["password"],
                singleUser[0]["password"],
            ],
            [
                "*** Create a new user account ***",
                "First name:",
                "Last name:",
                "Username:",
                "Password:",
                # "Some message about job being created"
            ],
            threeAccounts,
            3,
            singleUser[0]["username"],
        ),
    ],
    ids=[
        "CreateAccountOver5",
        "CreateAccountUnder5",
    ],
)
def testCreateAccount(
    mock_input, responses, startingUserDB, numUsers, expectedReturn, monkeypatch, capfd
):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    saveDatabase(JSON_USERS_FP, startingUserDB)
    userList = loadUsers()
    if numUsers is not None:
        # If error here, then the database is the issue not the create account logic
        assert len(userList) == numUsers
    try:
        assert printNewAccountScreen() == expectedReturn  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added



@pytest.mark.parametrize(
    "password_input",
    [
        "small",  # Too short
        "tkskadkkasdasdlsldlas",  # Too long
        "lowercase123!",  # No capital letter
        "UPPERCASEONLY!",  # No digit
        "NoSpecialChars1",  # No special character
    ],
    ids=[
        "TooShort",
        "TooLong",
        "NoCapital",
        "NoDigit",
        "NoSpecial",
    ],
)
def test_invalid_password_criteria(password_input, monkeypatch, capfd):
    saveDatabase(JSON_USERS_FP, threeAccounts)
    input_generator = iter(
        ["username", "TestFirstName", "TestLastName", password_input, password_input]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    error_message = "Password Requirements: minimum of 8 characters, maximum of 12 characters, at least 1 capital letter, at least 1 digit, at least 1 special character"
    assert error_message in captured.out


def test_saveUser_and_loadUsers_when_database_is_empty():
    # [] -> "database is empty"
    saveUser(
        [],
        singleUser[0]["username"],
        singleUser[0]["password"],
        singleUser[0]["firstname"],
        singleUser[0]["lastname"],
    )

    users = loadUsers()

    print(users)
    print(users[0])

    assert users[0] == singleUser[0]


def test_saveDatabase():
    # make sure DB is clean first:
    with open(JSON_USERS_FP, "w") as outfile:
        json.dump({}, outfile, indent=4)

    userList = [
        {
            "username": "admin",
            "password": "Password1!",
            "firstname": "Jo",
            "lastname": "Mama",
            "connections": [],
        },
        {
            "username": "tester",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["admin"],
        },
    ]

    print(userList)
    # print(userDB)

    saveDatabase(JSON_USERS_FP, userList)
    loadedUsers = loadUsers()
    # print("loadedusers", loadedUsers)
    print(loadUsers())

    assert loadedUsers == userList
