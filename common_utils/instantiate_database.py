import os

from pages.new_user_account import saveDatabase
from common_utils.utils import JSON_USERS_FP


userlist = [
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
    {
        "username": "admin2",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "connections": [],
    },
    {
        "username": "admin3",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "connections": []
    }
]


saveDatabase(JSON_USERS_FP, userlist)
