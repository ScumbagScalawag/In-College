from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase

# THIS IS JUST FOR TESTING STUFF UNOFFICIALLY. Feel free to delete if this bothers you -Noah

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
        "friendRequests": [],
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
        "friendRequests": [],
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
        "friendRequests": ["dummy"],
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
        "friendRequests": [],
    },
]


userDB = UserDatabase([])
userDB.addUserDictList(testDB)

print("---first toggle sms to false")
# UserDB.userlist[0] and user BOTH REFER TO THE SAME PLACE IN MEMORY, in this case
# Any changes to User must be written to DB's Json file, or else user will be changed only in memory:
# userDB.updateUser(user) 
user = userDB.userlist[0] # ^
user.toggleSmsSub()
print(user)
userDB.updateUser(user)
print(userDB)

print("---then toggle email to false")
user.toggleEmailSub()
print(user)
userDB.updateUser(user)
print(userDB)

print("---test updateuser with connection added")
print("Before Connection added", user)
user.sendFriendRequest("dummy")
print("After Connection added", user)
userDB.updateUser(user)
print("userDB after updating user: ", userDB)
loadedDB = UserDatabase()
loadedDB.loadUsers()
print("userDB after updating user: ", userDB)
print("loadedDB after updating user: ", loadedDB)


print("Database (in memory) is updated alongside user", userDB)
# Updates in-memory DB AND writes to Json
userDB.updateUser(user)


print("----Checking write to Json...")
userJsonDB = UserDatabase([])
userJsonDB.loadUsers()
print("JSON AFTER added connection", userJsonDB)


# print("-----testing user copy contructor")
# user1 = User.dictToUser(testDB[0])
# print("user1: ", user1)
# user2 = User.copy(user1)
# print("user2: ", user2)
# Ensure not same memory location (i.e. new obj)
# print(f"user1 location: {id(user1)}, user2 location: {id(user2)}")





