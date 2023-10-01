from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase

testDB = [
    {
        "username": "asdfasdf",
        "password": "P@ssw0rd",
        "firstname": "Noah",
        "lastname": "McIvor",
        "email": "nm@gmail.com",
        "phoneNumber": "1234567890",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "connections": [],
    },
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "dummy@gmail.com",
        "phoneNumber": "1234567890",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "connections": [],
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dee@gmail.com",
        "phoneNumber": "1234567890",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "connections": ["dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "connections": [],
    },
]


userDB = UserDatabase([])
userDB.addUserDictList(testDB)

print("---first toggle sms to false")
user = userDB.userlist[0]
user.toggleSmsSub()
print(user)
userDB.updateUser(user)
print(userDB)

print("---then toggle email to false")
user.toggleEmailSub()
print(user)
userDB.updateUser(user)
print(userDB)
