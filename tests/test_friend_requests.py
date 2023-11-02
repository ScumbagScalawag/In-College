import pytest

from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from pages.login import printLoginScreen
from tests.shared import fourAccounts, singleUser


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["y", ""],  # mock input
            [
                "You are now friends with sillyBoi",  # responses
            ],
            None,  # expected return
        ),
        (
            ["n", ""],  # these tests pass indiviudally, but not all together
            [
                "You have declined the friend request from sillyBoi",
            ],
            None,
        ),
        (
            ["X", ""],  # these tests pass indiviudally, but not all together
            [
                "Invalid input. Please enter 'y' or 'n': ",
            ],
            None,
        ),
    ],
    ids=["Accept", "Decline", "Invalid"],
)
def test_manageFriendRequest(mock_input, responses, expectedReturn, monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    #print(userDB.getUserDictList())
    testUser = userDB.getUser("dummy")
    # expectedReturn = None
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert manage_friend_requests(testUser, userDB) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out

    # assert that the friend request was actually removed
