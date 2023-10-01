from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from tests.shared import singleUser

tempUser = User(
    "tempUser",
    "P@ssw0rd",
    "Guy",
    "Dummy",
    "guydummy@gmail.com",
    "1234567890",
)

print(tempUser)


partiallyDefinedUser = User(
    username="tempUser",
    password="P@ssw0rd",
    firstname="Guy",
    lastname="Dummy2",
    email="guydummy@gmail.com",
    # phoneNumber="1234567890",
    smsSub=False,
)

print(partiallyDefinedUser)

partiallyDefinedUser.toggleSmsSub()

print(partiallyDefinedUser)

partiallyDefinedUser.username = "asdfasdf"
print(partiallyDefinedUser.username)
print(partiallyDefinedUser)

print(partiallyDefinedUser.toDict())

print("----userList")
userList: list[User] = []
userList.append(partiallyDefinedUser)
for user in userList:
    print(user)


print("---userDB")
userDB = UserDatabase(userList)
print(userDB.getDatabaseDict())


print("----userDict Logic")
userDictList = []
for user in userList:
    userDictList.append(user.toDict())
dictObject = {"userlist": userDictList}
print(dictObject)

print("--- appending to list")
userList.append(tempUser)
for user in userList:
    print(user)

print(userDB.getUserDictList())

userDB.saveDatabase()

print("----reading from empty DB")
# anotherUserList = []
secondDB = UserDatabase()  # empty UserDatabase object
secondDB.loadUsers()
print(secondDB.getDatabaseDict())

print("----testing addUser")
someUser = User(
    "thirdUserAdded",
    "P@ssw0rd",
    "Noah",
    "McIvor",
    "nm@gmail.com",
    "1234567890",
)

secondDB.addUser(someUser)
print(secondDB.getDatabaseDict())

print("----reading again")
readDB = UserDatabase()
print(readDB.getDatabaseDict())
readDB.loadUsers()
print(readDB.getDatabaseDict())

print(readDB.getUser(someUser.username))

print("----dictToUser()")
singleUserObject = User.dictToUser(singleUser)
print(singleUserObject)
print(readDB)
print(readDB.userlist[0])
