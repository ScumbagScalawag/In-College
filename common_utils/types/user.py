import json

from common_utils.types.exceptions import UnexpectedValueInUserAttribute


class User:
    SUPPORTED_LANGUAGES = ["English", "Spanish"]

    # Constructor (w/ default values)
    def __init__(
        self,
        username: str = "UNDEFINED",
        password: str = "UNDEFINED",
        firstname: str = "UNDEFINED",
        lastname: str = "UNDEFINED",
        email: str = "UNDEFINED",
        phoneNumber: str = "UNDEFINED",
        language: str = "English",
        emailSub: bool = True,
        smsSub: bool = True,
        adSub: bool = True,
        friends=[],
        friendRequests=[],
    ):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNumber = phoneNumber
        self.language = language
        self.emailSub = emailSub
        self.smsSub = smsSub
        self.adSub = adSub
        self.friends = friends
        self.friendRequests = friendRequests

    # Copy constructor: call like this: newUser = User.copy(userToCopy), where userToCopy: User
    # WARNING: This creates a NEW object (different place in memeory than original). It is NOT a reference to it
    @classmethod
    def copy(cls, userToCopy):
        return cls(
            username=userToCopy.username,
            password=userToCopy.password,
            firstname=userToCopy.firstname,
            lastname=userToCopy.lastname,
            email=userToCopy.email,
            phoneNumber=userToCopy.phoneNumber,
            language=userToCopy.language,
            emailSub=userToCopy.emailSub,
            smsSub=userToCopy.smsSub,
            adSub=userToCopy.adSub,
            friends=userToCopy.friends.copy(),
            friendRequests=userToCopy.friendRequests.copy(),  # Make a copy of the friendRequests list
        )
    
    # WARNING: This method only copies VALUES from otherUser: user2.copyValues(user1)
    def copyValues(self, otherUser):
        self.username = otherUser.username
        self.password = otherUser.password
        self.firstname = otherUser.firstname
        self.lastname = otherUser.lastname
        self.email = otherUser.email
        self.phoneNumber = otherUser.phoneNumber
        self.language = otherUser.language
        self.emailSub = otherUser.emailSub
        self.smsSub = otherUser.smsSub
        self.adSub = otherUser.adSub
        self.friends = otherUser.friends.copy()
        self.friendRequests = otherUser.friendRequests.copy()


    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression. otherUser is of type User
    def __eq__(self, otherUser) -> bool:
        # in case otherUser is None
        if not isinstance(otherUser, User):
            return False
        else:
            return self.username == otherUser.username

    # GETTERS

    # return the Dict translation
    def toDict(self):
        return {
            "username": self.username,
            "password": self.password,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "language": self.language,
            "emailSub": self.emailSub,
            "smsSub": self.smsSub,
            "adSub": self.adSub,
            "friends": self.friends,
            "friendRequests": self.friendRequests,
        }

    def hasPendingFriendRequest(self, username: str):
        if isinstance(username, str):
            for friendRequestUsername in self.friendRequests:
                if friendRequestUsername == username:
                    return True
        # for case where user(name) is None: 
        else:
            # TODO: make this throw TypeError
            return False

        return False

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToUser(cls, userDict):
        return cls(
            username=userDict.get("username", "UNDEFINED"),
            password=userDict.get("password", "UNDEFINED"),
            firstname=userDict.get("firstname", "UNDEFINED"),
            lastname=userDict.get("lastname", "UNDEFINED"),
            email=userDict.get("email", "UNDEFINED"),
            phoneNumber=userDict.get("phoneNumber", "UNDEFINED"),
            language=userDict.get("language", "English"),
            emailSub=userDict.get("emailSub", True),
            smsSub=userDict.get("smsSub", True),
            adSub=userDict.get("adSub", True),
            friends=userDict.get("friends", []),
            friendRequests=userDict.get("friendRequests", []),
        )

    def setLanguage(self, language):
        if language in self.SUPPORTED_LANGUAGES:
            self.language = language
        else:
            raise ValueError("Unsupported language")

    def toggleEmailSub(self):
        try:
            if self.emailSub == True:
                self.emailSub = False
            elif self.emailSub == False:
                self.emailSub = True
            else:
                raise UnexpectedValueInUserAttribute("emailSub")
        except UnexpectedValueInUserAttribute as e:
            print(f"Error: {e}")
            return False

        return True

    def toggleSmsSub(self):
        try:
            if self.smsSub == True:
                self.smsSub = False
            elif self.smsSub == False:
                self.smsSub = True
            else:
                raise UnexpectedValueInUserAttribute("smsSub")
        except UnexpectedValueInUserAttribute as e:
            print(f"Error: {e}")
            return False

        return True

    def toggleAdSub(self):
        try:
            if self.adSub == True:
                self.adSub = False
            elif self.adSub == False:
                self.adSub = True
            else:
                raise UnexpectedValueInUserAttribute("adSub")
        except UnexpectedValueInUserAttribute as e:
            print(f"Error: {e}")
            return False

        return True

    def sendFriendRequest(self, username: str):
        for friendRequestUsername in self.friendRequests:
            # if friendRequest already exists
            if username == friendRequestUsername:
                return 1
            # if you've put your own username
            if username == self.username:
                return 2

        self.friendRequests.append(username)

        return 0

    def unsendFriendRequest(self, username: str):
        if not self.hasPendingFriendRequest(username):
            return False

        self.friendRequests.remove(username)

        return True

    def acceptFriendRequest(self, username: str):
        self.friends.append(username)
