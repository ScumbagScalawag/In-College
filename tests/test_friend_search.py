import pytest

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.friend_search import (  # Search Screen here to preload database
    friendSearchOptionList,
    printFriendSearchScreen,
)
from tests.shared import fourAccounts, singleUser


@pytest.fixture
def user_db():
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    return userDB


@pytest.mark.parametrize(
    "mock_input, responses",
    [
        (
            ["Dee", "Snuts", "2", "Y", "X"],
            [
                *friendSearchOptionList,
                "is part of the InCollege system",
            ],
        ),
        (
            ["Jo", "Mama", "Y", "X"],
            [
                *friendSearchOptionList,
                "is part of the InCollege system",
                "Connection request sent",
            ],
        ),
        (
            ["Foam", "Earplugs", "Y", "X"],
            [
                *friendSearchOptionList,
                "They are not yet a part of the InCollege system yet",
            ],
        ),
        (
            ["2", "cs", "3", "Y", "X"],
            [
                *friendSearchOptionList,
                "is part of the InCollege system",
                "Connection request sent",
            ],
        ),
    ],
    ids=["Found User multiple", "Found User single", "Not Found User", "Search by Major"],
)
def testPrintFriendSearchScreen(monkeypatch, capfd, mock_input, responses, user_db):
    # in system
    testUser = User.dictToUser(singleUser)
    # userDB = UserDatabase([])
    # userDB.addUserDictList()
    user_db.saveDatabase()
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added

def testPrintFriendSearchUniversity(monkeypatch, capfd):
    testUser = User.dictToUser(singleUser)
    user_db = UserDatabase([])
    user_db.addUserDictList(fourAccounts)
    user_db.saveDatabase()
    # Not in system
    input_generator = iter(["3", "uf", "Y","X"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    responses = [
        *friendSearchOptionList,
        "is part of the InCollege system",
        "Connection request sent",
    ]
    for r in responses:
        assert r in captured.out  # Friend successfully added


def testPrintFriendSearchNotLoggedIn(monkeypatch, capfd):
    testUser = None
    # Not in system
    input_generator = iter(["Jo","Mama"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    responses = [
        *friendSearchOptionList,
        "is part of the InCollege system",
    ]
    for r in responses:
        assert r in captured.out  # Friend not found in system


def testPrintFriendSearchScreenCancel(monkeypatch, capfd):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)

    # Not in system
    input_generator = iter(
        ["Dee","Snuts","x"]  # x is used to cancel the search
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    responses = [
        *friendSearchOptionList,
        #"Input c to continue or x to return to menu",
    ]
    for r in responses:
        assert r in captured.out


def testPrintFriendSearchScreenInvalidSelection(monkeypatch, capfd):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)

    # Not in system
    input_generator = iter(
        [
            "Dee",
            "Snuts",
            "5",
            "2",
            "x",
        ]  # 5 is an invalid selection
    )
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    responses = [
        *friendSearchOptionList,
        "Invalid selection. Please choose a number from the list.",
    ]
    for r in responses:
        assert r in captured.out