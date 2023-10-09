from unittest.mock import patch

import pytest

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.login import printLoginScreen
from tests.shared import fourAccounts, singleUser


def testLogin_loggedIn(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)
    input_generator = iter(["asdfasdf", "P@ssw0rd"])
    responses = [
        "Please log out and log back in to change accounts",
    ]
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printLoginScreen(testUser) == testUser  # function == expected return
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    for r in responses:
        assert r in captured.out  # Friend not found in system


def testLogin_invalidUser(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)

    # test account not in database
    input_generator = iter(
        [
            "user5",
            "P@ssword1",
        ]
    )
    responses = [
        "Incorrect username / password, please try again",
    ]
    expectedReturn = None
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printLoginScreen() == expectedReturn  # function == expected return
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    for r in responses:
        assert r in captured.out  # Friend not found in system


def testLogin_validUser(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    input_generator = iter(["dummy", "Password1!"])
    responses = [
        "You have successfully logged in",
    ]
    expectedReturn = None
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printLoginScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    for r in responses:
        assert r in captured.out
