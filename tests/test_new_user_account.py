import json
from common_utils import utils as u
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.new_user_account import printNewAccountScreen, saveDatabase, saveUser
from tests.shared import JSON_USERS_FP, singleUser, threeAccounts, fiveAccounts
import pytest


def test_CreateAccountOver5(capfd, monkeypatch):
    # ensure DB is empty first
    userDB = UserDatabase([]) 
    # Load 5 accounts to Json
    # saveDatabase(JSON_USERS_FP, fiveAccounts)
    userDB.addUserDictList(fiveAccounts)

    # Confirm there are 5 accounts
    assert len(userDB.userlist) == 5

    # Test 6th account
    input_generator = iter(["user6", "Jesse", "Small", "P@ssword1", "P@ssword1"])
    # print("before 6th iteration input generator")
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    # print("after 6th iteration input generator")

    captured = capfd.readouterr()
    #userContext = printNewAccountScreen()
    try:
        userContext = printNewAccountScreen()
        # assert None, essentially -> no user context 
        assert not isinstance(userContext, User)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, come back later" in captured.out


def testCreateAccountUnder5(monkeypatch, capfd):
    # Make sure Json is clear
    userDB = UserDatabase([])
    # Test with 3 accounts
    userDB.addUserDictList(threeAccounts)

    # saveDatabase(JSON_USERS_FP, threeAccounts)

    input_generator = iter(
        [
            singleUser["username"],
            singleUser["firstname"],
            singleUser["lastname"],
            singleUser["password"],
            singleUser["password"],
        ]
    )
    # monkeypatch.setattr(builtins, "input", lambda : next(input_generator))
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        # captured = capfd.readouterr()
        userContext = printNewAccountScreen()
        # make sure printNewAccountScreen returns context correctly
        if isinstance(userContext, User):
            assert userContext.username == singleUser["username"]
        if not isinstance(userContext, User):
            print("Something went wrong assigning user context!")
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
    # ensure DB is empty first
    userDB = UserDatabase([]) 
    # Load 3 accounts to Json
    userDB.addUserDictList(threeAccounts)

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
    userDB = UserDatabase([])
    userDB.addUserDict(singleUser)

    assert userDB.userExists(singleUser["username"])


def test_saveDatabase():
    userDB = UserDatabase([])
    userDB.addUserDictList(threeAccounts)

    print("-----userDB:")
    print(userDB)
    # print(threeAccounts)
    print("-----threeAccounts:")
    print(json.dumps(threeAccounts, indent=4))

    assert userDB.getUserDictList() == threeAccounts