from types.user_database import UserDatabase


userDictList = [
    {
        "username": "admin",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "tester",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "Spanish",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
    },
]

userDB = UserDatabase()
userDB.addUserDictList(userDictList)
