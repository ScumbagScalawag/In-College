import pytest
from main import printNewAccountScreen, saveUser
import json

def test_max_users(capfd, monkeypatch):
    with open("user_file.json", "w") as f:
        f.write("{}")
    # Load 5 accounts to test maximum feature
    accounts = {
        "Andrew": "Valid123!",
        "Candy": "Valid123!",
        "Bandy": "Valid123!",
        "Sandy": "Valid123!",
        "fishy": "Valid123!"
    }
    for username, password in accounts.items():
        saveUser(username, password)
    with open("user_file.json", "r") as f:
        users_data = json.load(f)
    assert len(users_data) == 5
    # Test 6th account
    input_values = ["user6", "Password1@", "Password1@"]
    input_generator = iter(input_values)

    monkeypatch.setattr('builtins.input', lambda: next(input_generator))

    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    # Captures what is printed
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, please come back later" in captured.out


def test_create_account_when_less_than_5_users(monkeypatch, capfd):
    # Clear the user database before starting the test
    with open("user_file.json", "w") as f:
        f.write("{}")

    # Emulate a sequence of inputs
    input_generator = iter(["newUser", "Password1@", "Password1@"])

    # Use monkeypatch to replace the built-in input function with our generator
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))

    # Handle the StopIteration exception when our generator runs out of items
    try:
        printNewAccountScreen()
    except StopIteration:
        pass

    # Capture the standard output and error for assertion
    captured = capfd.readouterr()

    # Verify the main menu is printed
    main_menu = (
        "*** Main Menu ***\n"
        "1 - Search for a job\n"
        "2 - Find someone that you know\n"
        "3 - Learn a skill\n"
    )
    assert main_menu in captured.out
