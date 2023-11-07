import pytest
from common_utils.types.user_database import UserDatabase, manage_friend_requests
from tests.shared import fourAccounts

initial_data = list(fourAccounts[:])


@pytest.fixture(scope="function", autouse=True)
def user_db_with_data():
    userDB = UserDatabase([])
    userDB.addUserDictList(initial_data)
    yield userDB


def test_manageFriendRequestDecline(user_db_with_data, monkeypatch, capfd):
    userDB = user_db_with_data
    testUser = userDB.getUser("dummy")
    input_generator = iter(["n", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert manage_friend_requests(testUser, userDB) == None
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "You have declined the friend request from sillyBoi" in captured.out
