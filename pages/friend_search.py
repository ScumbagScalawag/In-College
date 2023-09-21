from common_utils.utils import clearScreen, loadUsers, userSearch

# user selected to find someone that you know
def printFriendSearchScreen(currentUser=None):
    users = loadUsers()
    while True:
        clearScreen()
        print("*** Find A Friend ***")
        print("")
        first = input("First name: ")
        last = input("Last name: ")
        # If found, display
        if userSearch(users, firstname=first, lastname=last):
            print("They are a part of the InCollege system")
            # If logged in, friend request?
            if currentUser != None:
                confirm = input("Would you like to make a connection with {} {}?".format(first, last)).upper()
                while confirm != "Y" and confirm != "N":
                    confirm = input("Please input (y/n): ").upper()

        else:
            print("They are not yet a part of the InCollege system yet")    
        
        # Allow return
        while True:
            confirm = input("Input c to continue or x to return to menu: ").upper()
            if confirm == "X":
                return
            elif confirm == "C":
                break
