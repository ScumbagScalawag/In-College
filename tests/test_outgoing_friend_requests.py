from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.outgoing_friend_requests import (  # Search Screen here to preload database
    outgoingFriendRequestOptions,
    printOutgoingFriendRequestsScreen,
)
from tests.shared import fourAccounts, singleUser


def testNoFriendRequests(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter([""])  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printOutgoingFriendRequestsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *outgoingFriendRequestOptions,
        """You currently have no outgoing friend requests. Use InCollege's "Find Friends" feature to expand your network!""",
        "Press any button to continue...",
    ]
    # current user has no friends, should get this message

    for r in responses:
        assert r in captured.out


def testFriendRequestDisplay(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])

    # Add mutual friends to dict
    fourAccountsWithFriends = fourAccounts[:]
    currentUsername = fourAccountsWithFriends[0]["username"]
    friendUsername = fourAccountsWithFriends[1]["username"]
    fourAccountsWithFriends[0]["friendRequests"] = [friendUsername]

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
            printOutgoingFriendRequestsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *outgoingFriendRequestOptions,
        "1 - {}".format(friendUsername),
        "X - Return to previous menu",
    ]
    # current user has 1 friend, should get this message

    for r in responses:
        assert r in captured.out


# if we have to test remove friend request when it is added in the future, can reuse code from test_friends.py but change it for outgoing_friend_requests
