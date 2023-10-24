from common_utils.types.user import User
from tests.shared import singleUser, fourAccounts
from pages.friend_search import (
    printFriendSearchScreen,
    friendSearchOptionList,
)  # Search Screen here to preload database
from common_utils.types.user_database import UserDatabase


# TODO Paramertirize the tests
def testFriendSearchInSystem(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(["Dee", "Snuts", "2", "Y", "X"])
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
        "part of the InCollege system",
        "Connection request sent",
    ]
    for r in responses:
        assert r in captured.out  # Friend successfully added

    # print(captured.out)


def testFriendSearchNotInSystem(monkeypatch, capfd):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)

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
        assert printFriendSearchScreen(testUser) == testUser  # Make sure printFriendSearchScreen returns user context
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
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
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
        assert printFriendSearchScreen() == None  # Tests edge cases of not logged in: ...() defaults to None
    except StopIteration:
        pass

def testFriendSearchByMajor(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(["2", "cs", "2", "Y", "X"])
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
        "part of the InCollege system",
        "Connection request sent",
    ]
    for r in responses:
        assert r in captured.out  # Friend successfully added

def testFriendSearchByUniversity(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(["3", "usf", "2", "Y", "X"])
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
        "part of the InCollege system",
        "Connection request sent",
    ]
    for r in responses:
        assert r in captured.out  # Friend successfully added
