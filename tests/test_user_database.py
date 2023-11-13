from typing import Type
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
    user1 = userDB.getUser("dummy")
    user2 = userDB.getUser("sillyBoi")
    try:
        userDB.addFriend(user1, user2)
    except TypeError as e:
        print(f"Error: {e}")
    except:
        print("Unknown Error occured while adding friend")

    if isinstance(user2, User) and isinstance(user1, User):
        assert "dummy" in user2.friends
        assert "sillyBoi" in user1.friends
    else:
        raise ValueError("User Not found")

    # make sure DB saved correctly:
    secondDB = UserDatabase()
    secondDB.loadUsers()

    dummyUser = secondDB.getUser("dummy")
    sillyBoiUser = secondDB.getUser("sillyBoi")

    if isinstance(dummyUser, User) and isinstance(sillyBoiUser, User):
        assert "sillyBoi" in dummyUser.friends
        assert "dummy" in sillyBoiUser.friends
        assert len(dummyUser.friends) == 1
        assert len(sillyBoiUser.friends) == 1
    else:
        raise ValueError("User Not found")


def test_removeFriend():
    # Setting up a freind link
    test_addFriend()

    userDB = UserDatabase()
    userDB.loadUsers()

    dummyUser = userDB.getUser("dummy")
    sillyBoiUser = userDB.getUser("sillyBoi")

    assert isinstance(dummyUser, User)
    assert isinstance(sillyBoiUser, User)

    try:
        userDB.removeFriend(dummyUser, sillyBoiUser)
    except TypeError as e:
        print(f"Error: {e}")
    except:
        print("Unexpected error occured while removing friend")

    assert "sillyBoi" not in dummyUser.friends
    assert "dummy" not in sillyBoiUser.friends


def test_acceptFriendRequest():
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)

    dummy = userDB.getUser("dummy")
    sillyBoi = userDB.getUser("sillyBoi")

    if dummy == None or sillyBoi == None:
        raise (ValueError("User not found in database"))

    userDB.acceptFriendRequest(sillyBoi, dummy)

    updatedDummy = userDB.getUser("dummy")
    assert updatedDummy != None
    assert len(updatedDummy.friends) == 1
    assert updatedDummy.friends[0] == "sillyBoi"
    assert "sillyBoi" not in updatedDummy.friendRequests

    updatedSillyBoi = userDB.getUser("sillyBoi")
    assert updatedSillyBoi != None
    assert len(updatedSillyBoi.friends) == 1
    assert updatedSillyBoi.friends[0] == "dummy"
    assert len(updatedSillyBoi.friendRequests) == 0
    assert "dummy" not in updatedSillyBoi.friendRequests
