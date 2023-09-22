import json
from common_utils import utils as u
from pages.new_user_account import printNewAccountScreen, saveDatabase, saveUser
from tests.shared import JSONFP2

singleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Noah",
    "lastname": "McIvor",
    "connections": [],
}


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
    userList = u.loadUsers()
    print(userList)
    assert len(userList) == 5

    # Test 6th account
    input_generator = iter(["user6", "Jesse", "Small", "P@ssword1", "P@ssword1"])
    # print("before 6th iteration input generator")
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    # print("after 6th iteration input generator")

    captured = capfd.readouterr()
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "All permitted accounts have been created, come back later" in captured.out


def test_saveUser_and_loadUsers_when_database_is_empty():
    # [] -> "database is empty"
    saveUser(
        [],
        singleUser["username"],
        singleUser["password"],
        singleUser["firstname"],
        singleUser["lastname"],
    )

    users = u.loadUsers()

    print(users)
    print(users[0])

    assert users[0] == singleUser


def test_saveDatabase():
    # make sure DB is clean first:
    with open(JSONFP2, "w") as outfile:
        json.dump({}, outfile, indent=4)

    userList = [
        {
            "username": "admin",
            "password": "Password1!",
            "firstname": "Jo",
            "lastname": "Mama",
            "connections": [],
        },
        {
            "username": "tester",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["admin"],
        },
    ]

    print(userList)
    # print(userDB)

    saveDatabase(JSONFP2, userList)
    loadedUsers = u.loadUsers()
    # print("loadedusers", loadedUsers)
    print(u.loadUsers())

    assert loadedUsers == userList
