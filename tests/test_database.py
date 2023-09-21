from common_utils import utils as u
from pages.new_user_account import saveDatabase, saveUser
import os
import json

JSONFP2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")

singleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Noah",
    "lastname": "McIvor",
    "connections": [],
}


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

    userDB = {"userlist": userList}

    saveDatabase(JSONFP2, userDB)
    users = u.loadUsers()

    assert users == userList
    

