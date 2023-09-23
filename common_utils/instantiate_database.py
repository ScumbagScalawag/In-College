import os

from pages.new_user_account import saveDatabase

JSONFP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")

userDB = {
    "userlist": [
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
}

saveDatabase(JSONFP, userDB)
