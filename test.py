import pytest
from main import printNewAccountScreen, saveUser
import json

def testCreateAccountOver5(capfd, monkeypatch):
    with open("user_file.json", "w") as f:
        f.write("{}")
    # Load 5 accounts to Json
    accounts = {
        "Andrew": "Valid123!",
        "Candy": "Valid123!",
        "Bandy": "Valid123!",
        "Sandy": "Valid123!",
        "fishy": "Valid123!"
    }
    #Confirm there is 5 accounts
    for username, password in accounts.items():
        saveUser(username, password)
    with open("user_file.json", "r") as f:
        users_data = json.load(f)
    assert len(users_data) == 5
    # Test 6th account
    input_generator = iter(["user6", "P@ssword1", "P@ssword1"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, please come back later" in captured.out