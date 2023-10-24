from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.friends import (  # Search Screen here to preload database
    friendScreenOptions,
    printFriendsScreen,
)
from tests.shared import fourAccounts, singleUser


def testNoFriends(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter([""])  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printFriendsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendScreenOptions,
        """You currently have no users in your network. Use InCollege's "Find Friends" feature to expand your network!""",
        "Press any button to continue...",
    ]
    # current user has no friends, should get this message

    for r in responses:
        assert r in captured.out


def testFriendDisplay(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])

    # Add mutual friends to dict
    fourAccountsWithFriends = fourAccounts[:]
    currentUsername = fourAccountsWithFriends[0]["username"]
    friendUsername = fourAccountsWithFriends[1]["username"]
    fourAccountsWithFriends[0]["friends"] = [friendUsername]
    fourAccountsWithFriends[1]["friends"] = [currentUsername]

    userDB.addUserDictList(fourAccountsWithFriends)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(fourAccountsWithFriends[0])

    input_generator = iter(
        [
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printFriendsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendScreenOptions,
        "1 - {}".format(friendUsername),
        "X - Return to previous menu",
    ]
    # current user has 1 friend, should get this message

    for r in responses:
        assert r in captured.out


def testFriendRemove(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])

    # Add mutual friends to dict
    fourAccountsWithFriends = fourAccounts[:]
    currentUsername = fourAccountsWithFriends[0]["username"]
    friendUsername = fourAccountsWithFriends[1]["username"]
    fourAccountsWithFriends[0]["friends"] = [friendUsername]
    fourAccountsWithFriends[1]["friends"] = [currentUsername]

    userDB.addUserDictList(fourAccountsWithFriends)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = userDB.getUser(currentUsername)

    input_generator = iter(
        [
            "1",
            " ",
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printFriendsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendScreenOptions,
        "1 - {}".format(friendUsername),
        "X - Return to previous menu",
        "Removing Friend...",
        "Friend Removed...",
        "Press any button to continue...",
    ]
    # current user has 1 friend, should get this message upon deleting

    for r in responses:
        assert r in captured.out

    # Get the 2 affected users
    currentUser = userDB.getUser(currentUsername).toDict()
    friendUser = userDB.getUser(friendUsername).toDict()

    # Assert that the friend was properly removed from both friends lists
    assert friendUsername not in currentUser["friends"]
    assert currentUsername not in friendUser["friends"]
