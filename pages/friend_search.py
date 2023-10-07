from typing import Optional
from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.exceptions import UserNotFoundException
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


# user selected to find someone that you know
def printFriendSearchScreen(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()

    while True:
        clearScreen()
        printOptionList(friendSearchOptionList)
        first = input("First name: ")
        last = input("Last name: ")
        # If found, display
        foundUser = userDB.userSearch(firstname=first, lastname=last)

        if foundUser != None:
            print("They are a part of the InCollege system")

            # If logged in, friend request?
            if currentUser != None:
                confirm = input(
                    "Would you like to make a connection with {} {}? (y/n)".format(first, last)
                ).upper()
                while True:
                    if confirm == "Y":
                        # Add connection to currenUser: no need for pre-emptive checks: cases are handled by method itself.
                        # all we need to do here is catch all the errors thrown 
                        try:
                            currentUser.sendFriendRequest(foundUser.username)
                        except ValueError as e:
                            print(f"Error: {e}")
                            print(anyButtonToContinueMessage())
                            input("")
                            break
                        except:
                            print(f"There was an unexpected problem while sending friend requests")
                            print(anyButtonToContinueMessage())
                            input("")
                            break

                        # Now, update the DB (object + Json)
                        try: 
                            userDB.updateUser(currentUser)
                        except UserNotFoundException as e:
                            # is thrown inside updateUser() if user not found
                            print(f"Error: {e}")
                            print(anyButtonToContinueMessage())
                            input("")
                            break
                        except:
                            print("Unknown Error Occured while updating the database")
                            print(anyButtonToContinueMessage())
                            input("")
                            break

                        print("Connection request sent")
                        break
                    elif confirm == "N":
                        break
                    else:
                        confirm = input("Please input y or n: ").upper()
            else:
                return currentUser
        # If not found, display
        else:
            print("They are not yet a part of the InCollege system yet")

        # Allow return
        while True:
            confirm = input("Input c to continue or x to return to menu: ").upper()
            if confirm == "X":
                return currentUser
            elif confirm == "C":
                break


friendSearchOptionList = [
    "*** Find A Friend ***",
    "Search for someone you know on InCollege",
]


# Depreciated by User.addConnection()
# def addConnection(users, currentUser, targetUser):
#     currentUserIndex = None
#     # doesn't let you add yourself
#     if currentUser == targetUser:
#         msg = "You cannot make a connection with yourself"
#         return msg
#     # get index of current user
#     for i, user in enumerate(users):
#         if user["username"] == currentUser:
#             currentUserIndex = i
#             break
#     # doesn't let you add someone you already added
#     if targetUser in users[currentUserIndex]["connections"]:
#         msg = "You are already connected with this user"
#         return msg
#     # adds target to connections list and updates file
#     users[currentUserIndex]["connections"].append(targetUser)
#     users = {"userlist": users}
#     with open(JSON_USERS_FP, "w") as outfile:
#         json.dump(users, outfile, indent=4)
#     msg = "Connection request sent"
#     return msg
