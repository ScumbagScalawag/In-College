import pytest
from common_utils.types.user import User
from tests.shared import JSON_USERS_FP, singleUser, fourAccounts
from pages.friend_search import (
    printFriendSearchScreen,
    friendSearchOptionList,
)  # Search Screen here to preload database
from pages.new_user_account import saveDatabase  # Used to setup database
import json
from common_utils.types.user_database import UserDatabase


# TODO Paramertirize the tests
def testFriendSearchInSystem(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(["Dee", "Snuts", "Y", "X"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printFriendSearchScreen(testUser) == testUser
        )  # assert printFriendSearchScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendSearchOptionList,
        "They are a part of the InCollege system",
        "Connection request sent",
    ]
    # for r in responses:
    #     print("----r:", r)
    #     print("----captured.out:", captured.out)
    #     assert r in captured.out  # Friend successfully added

    assert responses[0] in captured.out
    assert responses[1] in captured.out
    assert responses[2] in captured.out
    assert responses[3] in captured.out
    assert responses[4] in captured.out

    print(captured.out)


def testFriendSearchNotInSystem(monkeypatch, capfd):
    saveDatabase(JSON_USERS_FP, fourAccounts)
    # Not in system
    input_generator = iter(
        [
            "Foam",
            "Earplugs",
            "Y",
            "X",
        ]  # Y is not used will cause it to ask for input again of X or C
    )  # Note: Do not add a user "Foam Earplugs" into the test cases or this will not work as intended
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(singleUser[0]["username"]) == 0  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    responses = [
        *friendSearchOptionList,
        "They are not yet a part of the InCollege system yet",
    ]
    for r in responses:
        assert r in captured.out  # Friend not found in system


# TODO Needs fixing of both logic and test
# User not logged in handled with return to -1
def testFriendSearchNotLoggedIn(monkeypatch, capfd):
    saveDatabase(JSON_USERS_FP, fourAccounts)
    input_generator = iter(
        [
            "Jo",
            "Mama",
            "Y",
            "X",
        ]  # Y is not used will cause it to ask for input again of X or C
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen() == -1  # Tests edge cases of not logged in
    except StopIteration:
        pass
