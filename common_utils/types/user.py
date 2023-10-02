import json


class User:
    def __init__(
        self,
        username: str = "UNDEFINED",
        password: str = "UNDEFINED",
        firstname: str = "UNDEFINED",
        lastname: str = "UNDEFINED",
        email: str = "UNDEFINED",
        phoneNumber: str = "UNDEFINED",
        emailSub: bool = True,
        smsSub: bool = True,
        adSub: bool = True,
        connections=[],
    ):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNumber = phoneNumber
        self.emailSub = emailSub
        self.smsSub = smsSub
        self.adSub = adSub
        self.connections = connections

    # Copy constructor: call like this: newUser = User.copy(userToCopy), where userToCopy: User
    @classmethod
    def copy(cls, userToCopy):
        return cls(
            username=userToCopy.username,
            password=userToCopy.password,
            firstname=userToCopy.firstname,
            lastname=userToCopy.lastname,
            email=userToCopy.email,
            phoneNumber=userToCopy.phoneNumber,
            emailSub=userToCopy.emailSub,
            smsSub=userToCopy.smsSub,
            adSub=userToCopy.adSub,
            connections=userToCopy.connections.copy(),  # Make a copy of the connections list
        )

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
            "emailSub": self.emailSub,
            "smsSub": self.smsSub,
            "adSub": self.adSub,
            "connections": self.connections,
        }

    def isConnection(self, username: str):
        if isinstance(username, str):
            for connection in self.connections:
                if connection == username:
                    return True
        # for case where user(name) is None
        else:
            return False

        return False

    # These can be retrieved manually. like this: userObject.firstname
    # def getUsername(self):
    #     return self.username

    # def getFirstName(self):
    #     return self.firstname

    # def getLastName(self):
    #     return self.lastname

    # def getEmail(self):
    #     return self.email

    # def getPhoneNumber(self):
    #     return self.phoneNumber

    # def getConnections(self):
    #     return self.connections

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
            emailSub=userDict.get("emailSub", True),
            smsSub=userDict.get("smsSub", True),
            adSub=userDict.get("adSub", True),
            connections=userDict.get("connections", []),
        )

    # These can be set manually. like this: userObject.firstname = "asdf"
    # def setUsername(self, username: str):
    #     self.username = username

    # def setPassword(self, password: str):
    #     self.passoword = password

    # def setFirstname(self, firstname: str):
    #     self.firstname = firstname

    # def setLastname(self, lastname: str):
    #     self.lastname = lastname

    # def setEmail(self, email: str):
    #     self.email = email

    # def setPhoneNumber(self, phoneNumber: str):
    #     self.phoneNumber = phoneNumber

    def toggleEmailSub(self):
        if self.emailSub == True:
            self.emailSub = False
        elif self.emailSub == False:
            self.emailSub = True
        else:
            return False

        return True

    def toggleSmsSub(self):
        if self.smsSub == True:
            self.smsSub = False
        elif self.smsSub == False:
            self.smsSub = True
        else:
            return False

        return True

    def toggleAdSub(self):
        if self.adSub == True:
            self.adSub = False
        elif self.adSub == False:
            self.adSub = True
        else:
            return False

        return True

    def addConnection(self, username: str):
        for connection in self.connections:
            # if connection already exists
            if username == connection:
                return 1
            # if you've put your own username
            if username == self.username:
                return 2

        self.connections.append(username)

        return 0

    def removeConnection(self, username: str):
        if not self.isConnection(username):
            return False

        self.connections.remove(username)

        return True
