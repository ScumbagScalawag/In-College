import pytest

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from pages.login import printLoginScreen
from tests.shared import fourAccounts, singleUser


# Commented this out because for some reason database was acting up when parameterized test ran multiple times
#########################################################
# @pytest.mark.parametrize(
#     "mock_input,responses,expectedReturn",
#     [
#         (
#             ["y",""],  # mock input
#             [
#                 "You are now friends with sillyBoi",  # responses
#             ],
#             None,  # expected return
#         ),
#         (
#             ["n",""],
#             [
#                 "You have declined the friend request from sillyBoi",
#             ],
#             None,
#         ),
#         (
#             ["X",""],
#             [
#                 "Invalid input. Please enter 'y' or 'n': ",
#             ],
#             None,
#         ),
#     ],
#     ids=["Accept", "Decline", "Invalid"],
# )
# def test_manageFriendRequest(mock_input, responses, expectedReturn, monkeypatch, capfd):
#     userDB = UserDatabase()
#     userDB.addUserDictList(fourAccounts)
#     print(userDB.getUserDictList())
#     testUser = userDB.getUser("dummy")
#     # expectedReturn = None
#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert manage_friend_requests(testUser, userDB) == expectedReturn
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     for r in responses:
#         assert r in captured.out

#     #assert that the friend request was actually removed

def testIncomingFriendRequestAccept(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    print(userDB.getUserDictList())
    testUser = userDB.getUser("dummy")
    expectedReturn = None
    mock_input = ["y","",]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    responses = ["You are now friends with sillyBoi"]
    try:
        assert manage_friend_requests(testUser, userDB) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out

def testIncomingFriendRequestDecline(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    print(userDB.getUserDictList())
    testUser = userDB.getUser("dummy")
    expectedReturn = None
    mock_input = ["n","",]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    responses = ["You have declined the friend request from sillyBoi"]
    try:
        assert manage_friend_requests(testUser, userDB) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    print(captured.out)
    for r in responses:
        assert r in captured.out

def testIncomingFriendRequestInvalidInput(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    print(userDB.getUserDictList())
    testUser = userDB.getUser("dummy")
    expectedReturn = None
    mock_input = ["z",""]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    responses = ["Invalid input. Please enter 'y' or 'n': "]
    try:
        assert manage_friend_requests(testUser, userDB) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    print(captured.out)
    
    for r in responses:
        assert r in captured.out
