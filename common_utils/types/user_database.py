from typing import List, Optional
from common_utils.types.exceptions import MaximumNumberOfUsers, UserNotFoundException
from common_utils.types.user import User
from common_utils.utils import MAX_USERS
import json

from common_utils.utils import JSON_USERS_FP


# anything to do with Dict/dict is mostly there for testing purposes
# Rest of logic should be with the objects themselves


class UserDatabase:
    def __init__(self, userlist: Optional[List[User]] = None):
        if userlist is None:
            userlist = []
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
                userDBDict = json.load(database)
                # Goes through array of (user) dicts and converts them to array of User for self.userlist
                for userDict in userDBDict.get("userlist", []):
                    user = User.dictToUser(userDict)
                    self.userlist.append(user)
        except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
            # feel free to comment this message out. I find it helpful -noah
            print("WARNING: Cannot find JSON DataBase!")
            pass

    # UserDatabase Dictionary Object
    def getDatabaseDict(self):
        return {"userlist": self.getUserDictList()}

    # List of User Dictionaries
    def getUserDictList(self):
        userDictList = []
        for user in self.userlist:
            userDictList.append(user.toDict())
        return userDictList

    def userExists(self, username: str):
        for user in self.userlist:
            if user.username == username:
                return True

        return False

    # pass username, not User.
    def getUser(self, username: str) -> Optional[User]:
        for user in self.userlist:
            if user.username == username:
                return user

        return None

    def userSearch(self, firstname, lastname) -> Optional[User]:
        for user in self.userlist:
            if user.firstname == firstname and user.lastname == lastname:
                return user

        return None

    def login(self, username: str, password: str):
        for user in self.userlist:
            if user.username == username and user.password == password:
                return user

        return None

    # SETTERS
    # simply writes the in-memory DB stuff into JSON
    def saveDatabase(self):
        if len(self.userlist) > MAX_USERS:
            raise MaximumNumberOfUsers("Cannot Write to UserDatabase: Maximum number of users reached")
        with open(JSON_USERS_FP, "w") as outfile:
            json.dump(self.getDatabaseDict(), outfile, indent=4)

    # Use for modifying users or replacing
    # updates the DB entry for the user object you pass in: overwrites all values
    def updateUser(self, alteredUser: Optional[User]) -> Optional[User]:
        if isinstance(alteredUser, User):
            try:
                # Find the index i of the target User object in userlist
                for i, user in enumerate(self.userlist):
                    if user.username == alteredUser.username:
                        self.userlist[i].copyValues(alteredUser)
                        self.saveDatabase()
                        return
                raise UserNotFoundException("Couldn't find match for user")
            except UserNotFoundException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    # saveUser() -> addUser() for conventions sake
    # gets passed a User object
    def addUser(self, user: User):
        if len(self.userlist) < MAX_USERS:
            self.userlist.append(user)
            self.saveDatabase()
        else:
            raise MaximumNumberOfUsers("Maxumum number of users has been reached")

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

    # Because accept/decline friend request requires multi-user changes that must all happen,
    # they are a DB function until someone thinks of something more clever
    def acceptFriendRequest(self, sender: User, reciever: User):
        # ensuring you don't double-append
        if reciever.isFriend(sender.username):
            raise ValueError(f"{reciever} is already friends with {sender}")
        if sender.isFriend(reciever.username):
            raise ValueError(f"{sender} is already friends with {reciever}")

        # otherwise...
        sender.friends.append(reciever.username)
        reciever.friends.append(sender.username)

        sender.friendRequests.remove(reciever.username)

    def declineFriendRequest(self, sender: User, reciever: User):
        # remove the username of reciever from sender.friendRequests
        if sender.hasPendingFriendRequestTo(reciever.username):
            sender.removeFriendRequest(reciever.username)
        else:
            raise ValueError(
                f"{sender.username} has not sent a friend request to {reciever.username}"
            )
