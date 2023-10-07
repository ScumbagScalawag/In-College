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

    # make sure DB was saved correctly
    secondDB = UserDatabase()
    secondDB.loadUsers()
    assert secondDB.getUserDictList() == threeAccounts


def test_getUser():
    userDB = UserDatabase()
    userDB.addUserDictList(threeAccounts)

    dummy = userDB.getUser("dummy")
    assert isinstance(dummy, User)
    assert dummy.username == "dummy"

    dummy = userDB.getUser("sillyBoi")
    assert isinstance(dummy, User)
    assert dummy.username == "sillyBoi"

    dummy = userDB.getUser("dummyDude")
    assert isinstance(dummy, User)
    assert dummy.username == "dummyDude"

    dummy = userDB.getUser("userNotInDB")
    assert dummy is None



def test_addFriend():
    userDB = UserDatabase()
    userDB.addUserDictList(threeAccounts)

    dummyUser = userDB.getUser("dummy")
    sillyBoiUser = userDB.getUser("sillyBoi")

    assert isinstance(dummyUser, User)
    assert isinstance(sillyBoiUser, User)

    try: 
        userDB.addFriend(sillyBoiUser, dummyUser)
    except TypeError as e:
        print("One of the users passed to addFriend() wasn't found")
        print(f"Error: {e}")
    except:
        print("Problem using addfriend")

    assert len(sillyBoiUser.friends) == 1 
    assert len(dummyUser.friends) == 1 

    assert sillyBoiUser.username in dummyUser.friends
    assert "sillyBoi" in dummyUser.friends

    assert dummyUser.username in sillyBoiUser.friends
    assert "dummy" in sillyBoiUser.friends

    # making sure that stuff was saved to db:
    secondDB = UserDatabase()
    secondDB.loadUsers()

    dummyUser2 = secondDB.getUser("dummy")
    sillyBoiUser2 = secondDB.getUser("sillyBoi")

    assert isinstance(dummyUser2, User)
    assert isinstance(sillyBoiUser2, User)

    assert len(sillyBoiUser2.friends) == 1 
    assert len(dummyUser2.friends) == 1 

    assert sillyBoiUser2.username in dummyUser2.friends
    assert "sillyBoi" in dummyUser2.friends

    assert dummyUser2.username in sillyBoiUser2.friends
    assert "dummy" in sillyBoiUser2.friends
    

