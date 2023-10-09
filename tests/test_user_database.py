from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from tests.shared import singleUser, threeAccounts, fourAccounts


def test_defaultConstructor():
    userDB = UserDatabase()
    assert len(userDB.userlist) == 0


def test_loadUsers_and_saveDatabase():
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)
    print(userDB)


def test_addUser_and_loadUsers_when_database_is_empty():
    userDB = UserDatabase()
    user = User.dictToUser(singleUser)
    userDB.addUser(user)

    assert userDB.userExists(user.username)

    secondDB = UserDatabase()
    secondDB.loadUsers()

    assert len(secondDB.userlist) == 1
    assert secondDB.userlist[0].username == user.username


def test_saveDatabase():
    userDB = UserDatabase()
    userDB.addUserDictList(threeAccounts)

    assert userDB.getUserDictList() == threeAccounts
