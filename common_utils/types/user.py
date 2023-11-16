import json

from common_utils.types.message import Message
from common_utils.types.profile import Profile


class User:
    SUPPORTED_LANGUAGES = ["English", "Spanish"]

    # Constructor (w/ default values)
    def __init__(
        self,
        username: str = "UNDEFINED",
        password: str = "UNDEFINED",
        firstname: str = "UNDEFINED",
        lastname: str = "UNDEFINED",
        uni: str = "UNDEFINED",
        major: str = "UNDEFINED",
        plusSubscription: bool = False,
        email: str = "UNDEFINED",
        phoneNumber: str = "UNDEFINED",
        language: str = "English",
        emailSub: bool = True,
        smsSub: bool = True,
        adSub: bool = True,
        friends=[],
        friendRequests=[],
        profile=None,
        applicationDeleted="UNDEFINED",
        incomingMessages=[],
        unseenUsers=[],
        lastApplicationDate="UNDEFINED",
    ):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.uni = uni
        self.major = major
        self.plusSubscription = plusSubscription
        self.email = email
        self.phoneNumber = phoneNumber
        # self.language = language
        self.language = self.returnValidLanguage(language)
        self.emailSub = emailSub
        self.smsSub = smsSub
        self.adSub = adSub
        self.friends = friends
        self.friendRequests = friendRequests
        self.profile = Profile() if profile is None else profile
        self.applicationDeleted = applicationDeleted
        self.incomingMessages = incomingMessages
        self.unseenUsers = unseenUsers
        self.lastApplicationDate = lastApplicationDate

    # WARNING: This method only copies VALUES from otherUser: user2.copyValues(user1)
    def copyValues(self, otherUser):
        self.username = otherUser.username
        self.password = otherUser.password
        self.firstname = otherUser.firstname
        self.lastname = otherUser.lastname
        self.uni = otherUser.uni
        self.major = otherUser.major
        self.plusSubscription = otherUser.plusSubscription
        self.email = otherUser.email
        self.phoneNumber = otherUser.phoneNumber
        self.language = otherUser.language
        self.emailSub = otherUser.emailSub
        self.smsSub = otherUser.smsSub
        self.adSub = otherUser.adSub
        self.friends = otherUser.friends.copy()
        self.friendRequests = otherUser.friendRequests.copy()
        self.profile.copyValues(otherUser.profile)
        self.applicationDeleted = otherUser.applicationDeleted
        self.incomingMessages = otherUser.incomingMessages.copy()
        self.unseenUsers = otherUser.unseenUsers.copy()
        self.lastApplicationDate = otherUser.lastApplicationDate

    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression, where otherUser is of type User
    def __eq__(self, otherUser) -> bool:
        # in case otherUser is None
        if not isinstance(otherUser, User):
            return False
        else:
            return self.username == otherUser.username
            # return self.username == otherUser.username and self.password == otherUser.password and self.firstname == otherUser.firstname and self.lastname == otherUser.lastname and self.uni == otherUser.uni and self.major == otherUser.major and self.plusSubscription == otherUser.plusSubscription and self.email == otherUser.email and self.phoneNumber == otherUser.phoneNumber and self.language == otherUser.language and self.emailSub == otherUser.emailSub and self.smsSub == otherUser.smsSub and self.adSub == otherUser.adSub and self.friends == otherUser.friends and self.friendRequests == otherUser.friendRequests and self.profile == otherUser.profile and self.applicationDeleted == otherUser.applicationDeleted and self.incomingMessages == otherUser.incomingMessages

    # GETTERS

    # return the Dict translation
    def toDict(self):
        incomingMessagesDictList = []
        for message in self.incomingMessages:
            incomingMessagesDictList.append(message.toDict())
        return {
            "username": self.username,
            "password": self.password,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "uni": self.uni,
            "major": self.major,
            "plusSubscription": self.plusSubscription,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "language": self.language,
            "emailSub": self.emailSub,
            "smsSub": self.smsSub,
            "adSub": self.adSub,
            "friends": self.friends,
            "friendRequests": self.friendRequests,
            "profile": self.profile.toDict() if self.profile else None,
            "applicationDeleted": self.applicationDeleted,
            "incomingMessages": incomingMessagesDictList,
            "unseenUsers": self.unseenUsers,
            "lastApplicationDate": self.lastApplicationDate,
        }

    def hasPendingFriendRequestTo(self, username: str):
        if isinstance(username, str):
            if username in self.friendRequests:
                return True
        else:
            raise TypeError

        return False

    # Returns true if the user has unread messages, false otherwise
    def hasUnreadMessages(self):
        if len(self.incomingMessages) == 0:
            return False
        for message in self.incomingMessages:
            if message.read == False:
                return True
        return False

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToUser(cls, userDict):
        profile_data = userDict.get("profile")
        profile_obj = None
        if profile_data:
            profile_obj = Profile.dictToProfile(profile_data)

        incomingMessages = []
        incomingMessagesDictList = userDict.get("incomingMessages")
        if incomingMessagesDictList is not None:
            for message in incomingMessagesDictList:
                incomingMessages.append(Message.dictToMessage(message))

        return cls(
            username=userDict.get("username", "UNDEFINED"),
            password=userDict.get("password", "UNDEFINED"),
            firstname=userDict.get("firstname", "UNDEFINED"),
            lastname=userDict.get("lastname", "UNDEFINED"),
            uni=userDict.get("uni"),
            major=userDict.get("major"),
            plusSubscription=userDict.get("plusSubscription", False),
            email=userDict.get("email", "UNDEFINED"),
            phoneNumber=userDict.get("phoneNumber", "UNDEFINED"),
            language=userDict.get("language", "English"),
            emailSub=userDict.get("emailSub", True),
            smsSub=userDict.get("smsSub", True),
            adSub=userDict.get("adSub", True),
            friends=userDict.get("friends", []),
            friendRequests=userDict.get("friendRequests", []),
            profile=profile_obj,
            applicationDeleted=userDict.get("applicationDeleted", "UNDEFINED"),
            incomingMessages=incomingMessages,
            unseenUsers=userDict.get("unseenUsers", []),
            lastApplicationDate=userDict.get("lastApplicationDate", "UNDEFINED"),
        )

    def setLanguage(self, language: str):
        self.language = self.returnValidLanguage(language)

    def returnValidLanguage(self, language: str):
        if language in self.SUPPORTED_LANGUAGES:
            return language
        else:
            return "English"

    def toggleEmailSub(self):
        if not isinstance(self.emailSub, bool):
            raise TypeError("Unexptected type inside of emailSub property. Defaulting to True...")

        if self.emailSub == True:
            self.emailSub = False
        elif self.emailSub == False:
            self.emailSub = True

    def toggleSmsSub(self):
        if not isinstance(self.smsSub, bool):
            raise TypeError("Unexptected type inside of smsSub property. Defaulting to True...")

        if self.smsSub == True:
            self.smsSub = False
        elif self.smsSub == False:
            self.smsSub = True

    def toggleAdSub(self):
        if not isinstance(self.adSub, bool):
            raise TypeError("Unexptected type inside of adSub property. Defaulting to True...")

        if self.adSub == True:
            self.adSub = False
        elif self.adSub == False:
            self.adSub = True

    def sendFriendRequest(self, username: str):
        if username in self.friendRequests:
            raise ValueError("You have already sent that user a friend request")
        elif username in self.friends:
            raise ValueError("You are already friends with that user")
        elif username == self.username:
            raise ValueError("You cannot send a friend request to yourself")

        self.friendRequests.append(username)

    def removeFriendRequest(self, username: str):
        if not self.hasPendingFriendRequestTo(username):
            raise ValueError("Friend request to that user not found")

        self.friendRequests.remove(username)

    def isFriend(self, username: str):
        return username in self.friends

    def markMessageRead(self, index):
        # error handling
        if index < 0 or index >= len(self.incomingMessages):
            raise IndexError("Index out of range")
        else:
            self.incomingMessages[index].markRead()

    def deleteMessage(self, index):
        # error handling
        if index < 0 or index >= len(self.incomingMessages):
            raise IndexError("Index out of range")
        else:
            self.incomingMessages.pop(index)

    def appendToIncomingMessages(self, message):
        self.incomingMessages.append(message)

    def appendUnseen(self, firstnlast: str):
        self.unseenUsers.append(firstnlast)

    def setLastApplicationDate(self, date: str):
        self.lastApplicationDate = date

    # TEST UTILS
    # scans using all key/value pairs in expectedUserDict, then compares to user.
    # Does not test for values defined in "self" that are not in expectedUserDict
    def assertPropertiesEqualToDict(self, expectedUserDict):
        for propertyName, expectedValue in expectedUserDict.items():
            actualValue = getattr(self, propertyName)
            if propertyName == "profile":
                actualValue = actualValue.toDict()
            # Uncomment for more detailed info when debugging
            # print("actualValue:", actualValue)
            # print("expectedValue:", expectedValue)
            assert (
                actualValue == expectedValue
            ), f"Property '{propertyName}' is not equal to the expected value '{expectedValue}'"
