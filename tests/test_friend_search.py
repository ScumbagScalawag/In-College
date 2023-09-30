import pytest
from tests.shared import JSON_USERS_FP, singleUser, fourAccounts
from pages.friend_search import (
    printFriendSearchScreen,
    friendSearchOptionList,
)  # Search Screen here to preload database
from pages.new_user_account import saveDatabase  # Used to setup database
import json

# TODO Paramertirize the tests
def testFriendSearchInSystem(monkeypatch, capfd):
    # in system
    saveDatabase(JSON_USERS_FP, fourAccounts)
    input_generator = iter(
        [
            "Dee",
            "Snuts",
            "Y",
            "X",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(singleUser[0]["username"]) == 0  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendSearchOptionList,
        "They are a part of the InCollege system",
        "Connection request sent",
    ]
    for r in responses:
        assert r in captured.out  # Friend successfully added


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
