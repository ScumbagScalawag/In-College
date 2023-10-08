from typing import Optional
from common_utils.messages import anyButtonToContinueMessage, invalidInput
from common_utils.types.exceptions import UserNotFoundException
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList


# user selected to find someone that you know
def printFriendSearchScreen(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()
    while True:
        foundUser = None
        clearScreen()
        printOptionList(friendSearchOptionList)
        first = input("")
        if first == "2":  # Search by major
            major = input("Enter the major: ")
            foundUsers = userDB.userSearch(major=major)
        elif first == "3":  # Search by university
            uni = input("Enter the university: ")
            foundUsers = userDB.userSearch(uni=uni)
        else:  # Assume search by name
            last = input("Last name: ")
            foundUsers = userDB.userSearch(firstname=first, lastname=last)

        if foundUsers:
            if len(foundUsers) > 1:
                print("Users found ('First' 'Last' 'Username'):")
                for i, user in enumerate(foundUsers):
                    print(f"{i + 1}. {user.firstname} {user.lastname} {user.username}")
                while True:
                    selection = input("Select a user by number or press x to cancel: ")
                    if selection.lower() == 'x':
                        break
                    try:
                        selected_index = int(selection) - 1
                        if 0 <= selected_index < len(foundUsers):
                            foundUser = foundUsers[selected_index]
                            break
                        else:
                            print("Invalid selection. Please choose a number from the list.")
                    except ValueError:
                        print(invalidInput("Enter Whole number or X"))
            else:
                foundUser = foundUsers[0]  # only one user

        if foundUser != None:
            print("{} {} is part of the InCollege system".format(foundUser.firstname, foundUser.lastname))

            # If logged in, friend request?
            if currentUser != None:
                confirm = input(
                    "Would you like to make a connection {} {} ?(y/n)".format(foundUser.firstname, foundUser.lastname)
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
    "Default is First Name: (Enter 2 for Major, 3 for university)"
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
