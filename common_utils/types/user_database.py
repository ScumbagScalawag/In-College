from typing import List
from common_utils.types.user import User
import json

from common_utils.utils import JSON_USERS_FP


# anything to do with Dict/dict is mostly there for testing purposes
# Rest of logic should be with the objects themselves


class UserDatabase:
    def __init__(self, userlist: List[User] = []):
        self.userlist = userlist

    # Easily print userDB: UserDatabase -> print(userDB)
    def __str__(self):
        return json.dumps(self.getDatabaseDict(), indent=4)

    # GETTERS

    # load from JSON
    def loadUsers(self):
        self.userlist = []
        try:
            with open(JSON_USERS_FP, "r") as database:
                userDict = json.load(database)
                # Goes through array of (user) dicts and converts them to array of User for the object
                # self.userlist = [User(**userData) for userData in userDict.get("userlist", [])]
                # self.userlist = []
                for user_data in userDict.get("userlist", []):
                    user = User(
                        # second arg: default if key not found
                        username=user_data.get("username", "UNDEFINED"),
                        password=user_data.get("password", "UNDEFINED"),
                        firstname=user_data.get("firstname", "UNDEFINED"),
                        lastname=user_data.get("lastname", "UNDEFINED"),
                        email=user_data.get("email", "UNDEFINED"),
                        phoneNumber=user_data.get("phoneNumber", "UNDEFINED"),
                        emailSub=user_data.get("emailSub", True),
                        smsSub=user_data.get("smsSub", True),
                        adSub=user_data.get("adSub", True),
                        connections=user_data.get("connections", []),
                    )
                    self.userlist.append(user)
        except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
            # feel free to comment this message out. I find it helpful -noah
            print("WARNING: Cannot find JSON DataBase!")
            pass

    # Internal Dictionary Object - needed for easy printing to console: print(userDatabaseObject.getDatabaseDict())
    def getDatabaseDict(self):
        return {"userlist": self.getUserDictList()}

    # Internal Dictionary Object
    def getUserDictList(self):
        userDictList = []
        for user in self.userlist:
            userDictList.append(user.toDict())
        return userDictList

    def userExists(self, username):
        for user in self.userlist:
            if user.username == username:
                return True

        return False

    # pass username, not User.
    def getUser(self, username: str):
        for user in self.userlist:
            if user.username == username:
                return user

        return False

    # SETTERS
    # simply writes the in-memory DB stuff into JSON
    def saveDatabase(self):
        with open(JSON_USERS_FP, "w") as outfile:
            json.dump(self.getDatabaseDict(), outfile, indent=4)

    # saveUser() -> addUser() for conventions sake
    # gets passed a User object
    def addUser(self, user: User):
        self.userlist.append(user)
        self.saveDatabase()

    def addUserList(self, userList: List[User]):
        for user in userList:
            self.addUser(user)

    def addUserDict(self, userDict: dict):
        user = User.dictToUser(userDict)
        self.addUser(user)

    # Helpful for testing. Use this for tests.shared account mocks/fixtures
    def addUserDictList(self, userDictList: List[dict]):
        for userDict in userDictList:
            self.addUserDict(userDict)
