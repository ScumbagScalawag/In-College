import pytest
from common_utils.types.user import User
from tests.shared import UNEXPECTED_TESTING_ERROR_MESSAGE, nonDefualtsSingleUser, singleUser


def test_default_constructor():
    user = User()
    assert user.username == "UNDEFINED"
    assert user.password == "UNDEFINED"
    assert user.firstname == "UNDEFINED"
    assert user.lastname == "UNDEFINED"
    assert user.uni == "UNDEFINED"
    assert user.major == "UNDEFINED"
    assert user.email == "UNDEFINED"
    assert user.phoneNumber == "UNDEFINED"
    assert user.language == "English"
    assert user.emailSub == True
    assert user.smsSub == True
    assert user.adSub == True
    assert len(user.friends) == 0
    assert len(user.friendRequests) == 0


def test_copyValues():
    user1 = User.dictToUser(nonDefualtsSingleUser)
    user2 = User()
    user2.copyValues(user1)
    user2.assertPropertiesEqualToDict(nonDefualtsSingleUser)


# tests the __eq__() function, for testing if user1 == user2
def test_equals_comparison():
    user1 = User.dictToUser(singleUser)
    user2 = User.dictToUser(singleUser)
    # for now only check username
    assert user1 == user2


def test_supported_languages():
    user = User()
    # simply meant to ensure all language-related logic is changed if support increases
    assert len(user.SUPPORTED_LANGUAGES) == 2


def test_toDict():
    user1 = User.dictToUser(singleUser)
    userDict = user1.toDict()
    assert userDict == singleUser


def test_hasPendingFriendRequest():
    user = User.dictToUser(singleUser)
    assert user.hasPendingFriendRequestTo("someUser") == False

    user2 = User.dictToUser(nonDefualtsSingleUser)
    assert user2.hasPendingFriendRequestTo("anotherUser") == True


def test_dictToUser():
    dummyUser = User()
    print(dummyUser)
    user = User.dictToUser(nonDefualtsSingleUser)
    print(user)
    try:
        user.assertPropertiesEqualToDict(nonDefualtsSingleUser)
    except ValueError as e:
        print(f"Error: {e}")


def test_setLanguage():
    user = User.dictToUser(nonDefualtsSingleUser)

    user.setLanguage("English")
    assert user.language == "English"
    # Should Default to English if unsupported
    user.setLanguage("French")
    assert user.language == "English"
    user.setLanguage("English")
    assert user.language == "English"
    user.setLanguage("random Invalid Text")
    assert user.language == "English"


def test_returnValidLanguage():
    user = User.dictToUser(singleUser)
    assert user.returnValidLanguage("Spanish") == "Spanish"
    assert user.returnValidLanguage("English") == "English"
    # Returns English if invalid/unsupported language
    assert user.returnValidLanguage("French") == "English"
    assert user.returnValidLanguage("Russian") == "English"
    assert user.returnValidLanguage("") == "English"


def test_toggleEmailSub():
    user = User.dictToUser(nonDefualtsSingleUser)
    assert user.emailSub == False

    # Catch anything strange while testing
    try:
        user.toggleEmailSub()
    except TypeError as e:
        print(UNEXPECTED_TESTING_ERROR_MESSAGE)
        print(f"Error: {e}")

    assert user.emailSub == True

    user.emailSub = False
    assert user.emailSub == False

    # make sure error message is raisd when necessary
    user.emailSub = "SomeInvalidValueType"
    with pytest.raises(
        TypeError, match="Unexptected type inside of emailSub property. Defaulting to True..."
    ):
        user.toggleEmailSub()


def test_toggleSmsSub():
    user = User.dictToUser(nonDefualtsSingleUser)
    assert user.smsSub == False

    # Catch anything strange while testing
    try:
        user.toggleSmsSub()
    except TypeError as e:
        print(UNEXPECTED_TESTING_ERROR_MESSAGE)
        print(f"Error: {e}")

    assert user.smsSub == True

    user.smsSub = False
    assert user.smsSub == False

    # make sure error message is raisd when necessary
    user.smsSub = "SomeInvalidValueType"
    with pytest.raises(
        TypeError, match="Unexptected type inside of smsSub property. Defaulting to True..."
    ):
        user.toggleSmsSub()


def test_toggleAdSub():
    user = User.dictToUser(nonDefualtsSingleUser)
    assert user.adSub == False

    # Catch anything strange while testing
    try:
        user.toggleAdSub()
    except TypeError as e:
        print(UNEXPECTED_TESTING_ERROR_MESSAGE)
        print(f"Error: {e}")

    assert user.adSub == True

    user.adSub = False
    assert user.adSub == False

    # make sure error message is raisd when necessary
    user.adSub = "SomeInvalidValueType"
    with pytest.raises(
        TypeError, match="Unexptected type inside of adSub property. Defaulting to True..."
    ):
        user.toggleAdSub()


def test_sendFriendRequest():
    user = User.dictToUser(nonDefualtsSingleUser)

    # Testing that sendFriendRequest raises the correct ValueError messages: we expect error to throw in these cases
    with pytest.raises(ValueError, match="You have already sent that user a friend request"):
        user.sendFriendRequest("someOtherUser")

    with pytest.raises(ValueError, match="You are already friends with that user"):
        user.sendFriendRequest("someUser")

    with pytest.raises(ValueError, match="You cannot send a friend request to yourself"):
        user.sendFriendRequest("asdfasdf")

    validUname = "aValidUsername"
    user.sendFriendRequest(validUname)
    assert validUname in user.friendRequests


def test_removeFriendRequest():
    user = User.dictToUser(nonDefualtsSingleUser)
    otherUser = "someOtherUser"
    assert otherUser in user.friendRequests

    try:
        user.removeFriendRequest(otherUser)
    except TypeError as e:
        print(UNEXPECTED_TESTING_ERROR_MESSAGE)
        print(f"Error: {e}")

    assert otherUser not in user.friendRequests

    with pytest.raises(ValueError, match="Friend request to that user not found"):
        user.removeFriendRequest("usernameNotInFriendRequestList")


def test_isFriend():
    user = User.dictToUser(nonDefualtsSingleUser)
    assert user.isFriend("someUser")
    assert not user.isFriend("randomUserName92")


def test_assertPropertiesEqualToDict():
    user = User.dictToUser(nonDefualtsSingleUser)
    user.assertPropertiesEqualToDict(nonDefualtsSingleUser)
