import pytest
import json
from common_utils.types.user import User
from common_utils.types.message import Message
from common_utils.types.user_database import UserDatabase
from pages.messaging import printMessagingScreen
from tests.shared import JSON_USERS_FP, test_users_data_message


@pytest.fixture
def setup_users():
    # Read and save the original data
    with open(JSON_USERS_FP, 'r') as file:
        original_data = json.load(file)

    # Write the test users to the JSON file
    with open(JSON_USERS_FP, 'w') as file:
        json.dump(test_users_data_message, file, indent=4)

    # Create UserDatabase instance with test users
    test_users = [User.dictToUser(user_dict) for user_dict in test_users_data_message['userlist']]
    user_db = UserDatabase(userlist=test_users)

    yield user_db  # This is where the testing happens

    # # After the test, restore the original data
    # with open(JSON_USERS_FP, 'w') as file:
    #     json.dump(original_data, file, indent=4)


def test_send_message(setup_users, monkeypatch):
    # Use the user database from the fixture
    user_db = setup_users

    # Mock the input function to return a predefined message subject and body
    input_values = iter(["Test Subject", "Hello! This is a test message.", "SEND"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    sender = user_db.getUser("user1")
    recipient = user_db.getUser("user2")
    message = Message(sender.username, recipient.username, "Test Subject", "Hello! This is a test message.")

    user_db.addMessage(message)

    recipient_after = user_db.getUser("user2")
    assert any(msg.message == "Hello! This is a test message." for msg in
               recipient_after.incomingMessages), "Message was not found in recipient's inbox"


def test_send_message_non_plus_to_non_friend(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user = user_db.getUser("user2")  # A non-plus user
    plus_user = user_db.getUser("user1")  # A plus user
    inputs = iter([
        "1","3"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        printMessagingScreen(non_plus_user)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "That feature is only available for InCollege Plus members" in captured.out


def test_send_message_non_plus_to_friend(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user_one = user_db.getUser("user2")  # A non-plus user
    non_plus_user_two = user_db.getUser("user3")  # Another non-plus user, presumably a friend

    inputs = iter(["1", "2", "1", "Test subject", "Test Message", "SEND"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        printMessagingScreen(non_plus_user_one)
    except StopIteration:
        pass

    # JSON needs to be reread for reasons
    with open(JSON_USERS_FP, 'r') as file:
        data_after_test = json.load(file)
    recipient_data = next((user for user in data_after_test['userlist'] if user['username'] == "user3"))
    last_message = recipient_data['incomingMessages'][-1]
    assert last_message[
               'message'].strip() == "Test Message\nSEND"

def test_respond_back(setup_users, monkeypatch, capfd):
    user_db = setup_users
    non_plus_user_one = user_db.getUser("user3")

    inputs = iter([
        "2", "1", "1", "y","subject:sendback", "trying to send body", "SEND"
    ])

    def mock_input(prompt=""):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)

    try:
        printMessagingScreen(non_plus_user_one)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    with open(JSON_USERS_FP, 'r') as file:
        data_after_test = json.load(file)
    recipient_data = next((user for user in data_after_test['userlist'] if user['username'] == "user2"))
    last_message = recipient_data['incomingMessages'][-1]
    assert last_message[
               'message'].strip() == "trying to send body\nSEND"