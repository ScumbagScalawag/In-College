from common_utils.utils import clearScreen
from pages.job_search import printJobSearchScreen
from pages.friend_search import printFriendSearchScreen
from pages.skill_search import printSkillScreen


# User has logged in menu
def printMainMenu():
    clearScreen()
    while True:
        print("*** Main Menu ***")
        print("1 - Search for a job")
        print("2 - Find someone that you know")
        print("3 - Learn a skill")
        print("4 - Log Out") # TODO: make common helper function to assign consistent logout symbol, like "X" -noah
        userInput = input()
        if userInput == "1":
            printJobSearchScreen()
        elif userInput == "2":
            print("under construction")
            printFriendSearchScreen()
        elif userInput == "3":
            printSkillScreen()
        elif userInput == "4":
            break
        else:
            print('Invalid selection please input "1" or "2" or "3"')

    return