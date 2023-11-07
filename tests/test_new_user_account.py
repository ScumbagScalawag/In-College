import pytest

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.new_user_account import printNewAccountScreen
from tests.shared import singleUser, tenAccounts, threeAccounts


# def test_CreateAccountOver10(capfd, monkeypatch):
#     # ensure DB is empty first
#     userDB = UserDatabase()
#     print(userDB)
#     # Load 5 accounts to Json
#     # saveDatabase(JSON_USERS_FP, fiveAccounts)
#     userDB.addUserDictList(tenAccounts)

#     # Confirm there are 10 accounts
#     assert len(userDB.userlist) == 10

#     # Test 11th account
#     input_generator = iter(["user11", "Jesse", "Small", "P@ssword1", "P@ssword1"])
#     # print("before 11th iteration input generator")
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     # print("after 11th iteration input generator")

#     captured = capfd.readouterr()
#     # userContext = printNewAccountScreen()
#     try:
#         userContext = printNewAccountScreen()
#         # assert None, essentially -> no user context
#         assert not isinstance(userContext, User)
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     assert "All permitted accounts have been created, come back later" in captured.out


# def testCreateAccountUnder10(monkeypatch, capfd):
#     # Make sure Json is clear
#     userDB = UserDatabase([])
#     # Test with 3 accounts
#     userDB.addUserDictList(threeAccounts)

#     # saveDatabase(JSON_USERS_FP, threeAccounts)

#     input_generator = iter(
#         [
#             singleUser["username"],
#             singleUser["firstname"],
#             singleUser["lastname"],
#             singleUser["password"],
#             singleUser["password"],
#         ]
#     )
#     # monkeypatch.setattr(builtins, "input", lambda : next(input_generator))


@pytest.mark.parametrize(
    "mock_input,responses,startingUserDB,numUsers,expectedReturn",
    [
        (
            ["user11", "Jesse", "Small", "P@ssword1", "P@ssword1", "anything"],
            [
                "All permitted accounts have been created, come back later",
                anyButtonToContinueMessage(),
            ],
            tenAccounts,
            10,
            -1,
        ),
        (
            [
                singleUser["username"],
                singleUser["firstname"],
                singleUser["lastname"],
                singleUser["password"],
                singleUser["password"],
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
            singleUser["username"],
        ),
    ],
    ids=[
        "CreateAccountOver10",
        "CreateAccountUnder10",
    ],
)
def testCreateAccount(
    mock_input, responses, startingUserDB, numUsers, expectedReturn, monkeypatch, capfd
):
    userDB = UserDatabase([])
    userDB.addUserDictList(startingUserDB)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    # if numUsers is not None:
    # If error here, then the database is the issue not the create account logic
    # assert len(userList) == numUsers
    try:
        # captured = capfd.readouterr()
        userContext = printNewAccountScreen()
        # make sure printNewAccountScreen returns context correctly
        if isinstance(userContext, User):
            assert userContext.username == singleUser["username"]
        if not isinstance(userContext, User):
            print(
                "Something went wrong assigning user context!"
            )  # TODO There should not be any prints in tests
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
    # ensure DB is empty first
    userDB = UserDatabase([])
    # Load 3 accounts to Json
    userDB.addUserDictList(threeAccounts)

    input_generator = iter(
        [
            "username",
            "TestFirstName",
            "TestLastName",
            "TestUniversity",
            "TestMajor",
            password_input,
            password_input,
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    error_message = "Password Requirements: minimum of 8 characters, maximum of 12 characters, at least 1 capital letter, at least 1 digit, at least 1 special character"
    assert error_message in captured.out
