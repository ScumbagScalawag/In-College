from typing import Optional
from common_utils.types.user import User
from common_utils.utils import clearScreen, printOptionList
from pages.friend_search import printFriendSearchScreen
from pages.job_search import printJobSearchScreen
from pages.skill_search import printSkillScreen


# User has logged in menu
def printMainMenu(currentUser: Optional[User]) -> Optional[User]:
    clearScreen()
    while True:
        printOptionList(mainMenuOptionsList)
        userInput = input("")
        if userInput == "1":
            currentUser = printJobSearchScreen(currentUser)
        elif userInput == "2":
            currentUser = printFriendSearchScreen(currentUser)
        elif userInput == "3":
            currentUser = printSkillScreen(currentUser)
        elif userInput.upper() == "X":
            print("Exiting InCollege")
            break
        else:
            print('Invalid selection please input "1" or "2" or "3"')

    return currentUser


mainMenuOptionsList = [
    "*** Main Menu ***",
    "1 - Search for a job",
    "2 - Find someone that you know",
    "3 - Learn a skill",
    "X - Log Out",
]
