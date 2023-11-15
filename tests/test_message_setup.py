import pytest
import json
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.messaging import printMessagingScreen
from tests.shared import JSON_USERS_FP, test_users_data_message


@pytest.fixture
def setup_users():
    # Read and save the original data
    with open(JSON_USERS_FP, "r") as file:
        original_data = json.load(file)

    # Write the test users to the JSON file
    with open(JSON_USERS_FP, "w") as file:
        json.dump(test_users_data_message, file, indent=4)

    # Create UserDatabase instance with test users
    test_users = [User.dictToUser(user_dict) for user_dict in test_users_data_message["userlist"]]
    user_db = UserDatabase(userlist=test_users)

    yield user_db  # This is where the testing happens

    with open(JSON_USERS_FP, "w") as file:
        json.dump(original_data, file, indent=4)


# inbox tests
def test_inbox(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user = user_db.getUser("user3")  # A non-plus user
    inputs = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    try:
        printMessagingScreen(non_plus_user)
    except StopIteration:
        pass
    user_db.saveDatabase()
    captured = capfd.readouterr()
    assert "WaterBoar" in captured.out and non_plus_user.incomingMessages[-1].subject == "WaterBoar"


# inbox tests
def test_inbox_marked_read(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user = user_db.getUser("user3")  # A non-plus user
    inputs = iter(["2", "1", "1", "n"])

    def mock_input(prompt=""):
        return next(inputs)

    monkeypatch.setattr("builtins.input", mock_input)

    try:
        printMessagingScreen(non_plus_user)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    user_db.saveDatabase()

    assert "[x] From" in captured.out and non_plus_user.incomingMessages[-1].read == True


# inbox tests
def test_inbox_delete(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user = user_db.getUser("user3")  # A non-plus user
    inputs = iter(["2", "1", "2", "n"])

    def mock_input(prompt=""):
        return next(inputs)

    monkeypatch.setattr("builtins.input", mock_input)

    try:
        printMessagingScreen(non_plus_user)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    user_db.saveDatabase()
    assert non_plus_user.incomingMessages == []


# inbox tests
def test_inbox_exit(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user = user_db.getUser("user3")  # A non-plus user
    inputs = iter(["2", "1", "x"])

    def mock_input(prompt=""):
        return next(inputs)

    monkeypatch.setattr("builtins.input", mock_input)

    try:
        printMessagingScreen(non_plus_user)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    user_db.saveDatabase()
    assert "[ ] From" in captured.out and non_plus_user.incomingMessages[-1].read == False
