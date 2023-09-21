import pytest
from common_utils.utils import loadUsers
from pages.new_user_account import printNewAccountScreen, saveEntireUserDataBase

def testCreateAccountOver5(capfd, monkeypatch):
    saveEntireUserDataBase({})
    # Load 5 accounts to Json
    accounts = {
        "Andrew": "Valid123!",
        "Candy": "Valid123!",
        "Bandy": "Valid123!",
        "Sandy": "Valid123!",
        "fishy": "Valid123!"
    }
    #Confirm there are 5 accounts
    saveEntireUserDataBase(accounts)
    userDataBase = loadUsers()
    assert len(userDataBase) == 5

    # Test 6th account
    input_generator = iter(["user6", "P@ssword1", "P@ssword1"])
    print("before 6th iteration input generator")
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    print("after 6th iteration input generator")

    captured = capfd.readouterr()
    printNewAccountScreen()
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, and come back later" in captured.out


