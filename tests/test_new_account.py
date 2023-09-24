import json
from common_utils import utils as u
from pages.new_user_account import printNewAccountScreen, saveDatabase, saveUser
from tests.shared import JSONFP2, singleUser, threeAccounts, fiveAccounts
import pytest


def test_CreateAccountOver5(capfd, monkeypatch):
    # ensure DB is empty first
    saveDatabase(JSONFP2, [])
    # Load 5 accounts to Json
    saveDatabase(JSONFP2, fiveAccounts)

    # Confirm there are 5 accounts
    userList = u.loadUsers()
    print(userList)
    assert len(userList) == 5

    # Test 6th account
    input_generator = iter(["user6", "Jesse", "Small", "P@ssword1", "P@ssword1"])
    # print("before 6th iteration input generator")
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    # print("after 6th iteration input generator")

    captured = capfd.readouterr()
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, come back later" in captured.out


def testCreateAccountUnder5(monkeypatch, capfd):
    # Make sure Json is clear
    # Test with 3 accounts

    saveDatabase(JSONFP2, threeAccounts)

    input_generator = iter(["usernew", "Johnathan", "Blow", "P@ssw0rd", "P@ssw0rd"])
    # monkeypatch.setattr(builtins, "input", lambda : next(input_generator))
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        # captured = capfd.readouterr()
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()

    title = "*** Create a new user account ***\n"
    firstname = "First name:"
    lastname = "Last name:"
    username = "Username:"
    password = "Password:"

    # Better approach than whole-sale output assertions
    assert title in captured.out
    assert firstname in captured.out
    assert lastname in captured.out
    assert username in captured.out
    assert password in captured.out


@pytest.mark.parametrize(
    "password_input",
    [
        "small",  # Too short
        "tkskadkkasdasdlsldlas",  # Too long
        "lowercase123!",  # No capital letter
        "UPPERCASEONLY!",  # No digit
        "NoSpecialChars1",  # No special character
    ],
    ids=["TooShort", "TooLong", "NoCapital", "NoDigit", "NoSpecial"],
)
def test_invalid_password_criteria(password_input, monkeypatch, capfd):
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
        singleUser["username"],
        singleUser["password"],
        singleUser["firstname"],
        singleUser["lastname"],
    )

    users = u.loadUsers()

    print(users)
    print(users[0])

    assert users[0] == singleUser


def test_saveDatabase():
    # make sure DB is clean first:
    with open(JSONFP2, "w") as outfile:
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

    saveDatabase(JSONFP2, userList)
    loadedUsers = u.loadUsers()
    # print("loadedusers", loadedUsers)
    print(u.loadUsers())

    assert loadedUsers == userList
