import os

from pages.new_user_account import saveDatabase
from common_utils.utils import JSON_USERS_FP


userDB = {
    "userlist": [
        {
            "username": "admin",
            "password": "Password1!",
            "firstname": "Jo",
            "lastname": "Mama",
            "email": "asdfasdf@gmail.com",
            "phoneNumber": "1932930298",
            "emailSub": True,
            "smsSub": True,
            "adSub": True,
            "connections": [],
        },
        {
            "username": "tester",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "email": "asdfasdf@gmail.com",
            "phoneNumber": "1932930298",
            "emailSub": True,
            "smsSub": True,
            "adSub": True,
            "connections": ["admin"],
        },
    ]
}

saveDatabase(JSON_USERS_FP, userDB)
