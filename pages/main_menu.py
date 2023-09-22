from common_utils.utils import clearScreen
from pages.job_search import printJobSearchScreen
from pages.friend_search import printFriendSearchScreen
from pages.skill_search import printSkillScreen


# User has logged in menu
def printMainMenu(currentUser):
    clearScreen()
    while True:
        print("*** Main Menu ***")
        print("1 - Search for a job")
        print("2 - Find someone that you know")
        print("3 - Learn a skill")
        print("X - Log Out")
        userInput = input()
        if userInput == "1":
            printJobSearchScreen()
        elif userInput == "2":
            print("under construction")
            printFriendSearchScreen(currentUser)
        elif userInput == "3":
            printSkillScreen()
        elif userInput.upper() == "X":
            print("Exiting InCollege")
            break
        else:
            print('Invalid selection please input "1" or "2" or "3"')

    return 0
