import pytest
from pages.initial_screen import printInitialScreen
import json

# Make sure DB remains unchanged, needs only 1 open slot to be tested correctly
@pytest.fixture
def restore():
    with open("../user_file.json", "r") as file:
        original_data = file.read()

    yield

    with open("../user_file.json", "w") as file:
        file.write(original_data)


# Checks if first name and last name prompt is given and if it exists in the database
def test_asking_first_and_last(monkeypatch, capfd, restore):
    input_generator = iter(["E", "2", "User_test", "First_test", "Last_test", "Password1!", "Password1!"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))

    try:
        printInitialScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "Username:" in captured.out
    assert "First name:" in captured.out
    assert "Last name:" in captured.out

    with open("../user_file.json", "r") as file:
        users_data = json.load(file)["userlist"]
        user_find = {}
        for user in users_data:
            if user["username"] == "User_test":
                user_find = user
                break
        assert user_find.get("firstname") == "First_test"
        assert user_find.get("lastname") == "Last_test"
