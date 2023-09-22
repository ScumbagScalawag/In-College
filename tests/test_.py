import pytest
from common_utils.utils import loadUsers
from pages.new_user_account import printNewAccountScreen, saveDatabase
from tests.shared import JSONFP2


def test_CreateAccountOver5(capfd, monkeypatch):
    # ensure DB is empty first
    saveDatabase(JSONFP2, [])
    # Load 5 accounts to Json

    fiveAccounts = [
        {
            "username": "dummy",
            "password": "Password1!",
            "firstname": "Jo",
            "lastname": "Mama",
            "connections": [],
        },
        {
            "username": "sillyBoi",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["notKaren", "dummy"],
        },
        {
            "username": "dummyDude",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["admin"],
        },
        {
            "username": "notKaren",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["dummy"],
        },
        {
            "username": "theSilliestOfAll",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": [""],
        },
    ]

    saveDatabase(JSONFP2, fiveAccounts)

    # Confirm there are 5 accounts
    
    userList = loadUsers()
    print(userList)
    assert len(userList) == 5

    # Test 6th account
    input_generator = iter(["user6", "P@ssword1", "P@ssword1"])
    # print("before 6th iteration input generator")
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    # print("after 6th iteration input generator")

    captured = capfd.readouterr()
    printNewAccountScreen()
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, come back later" in captured.out
