from common_utils.utils import clearScreen
from pages.under_construction import underConstructionMessage

SKILL_LIST = [
    {"name": "Skating", "desc": underConstructionMessage()},
    {"name": "Cooking", "desc": underConstructionMessage()},
    {"name": "Driving", "desc": underConstructionMessage()},
    {"name": "Painting", "desc": underConstructionMessage()},
    {"name": "Whistling", "desc": underConstructionMessage()},
]


def skillOptionsList():
    return [
        "*** Learn a skill ***",
        "1 - Learn how to skate",
        "2 - Learn how to cook",
        "3 - Learn how to drive",
        "4 - Learn how to paint",
        "5 - Learn how to whistle",
        "6 - Return to main menu",
    ]


# user has selected to "Learn a skill"
def printSkillScreen():
    clearScreen()
    skills = skillOptionsList()
    while True:
        for skill in skills:
            print(skill)
        userInput = input("")
        if userInput == "1":
            printSkillFromList("Skating")
        elif userInput == "2":
            printSkillFromList("Cooking")
        elif userInput == "3":
            printSkillFromList("Driving")
        elif userInput == "4":
            printSkillFromList("Painting")
        elif userInput == "5":
            printSkillFromList("Whistling")
        elif userInput == "6":
            break  # returns to caller (main menu) when you "exit"
        else:
            print('Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"')

    return 0


# TODO: make these functions a single generic function  -noah
# Used with printSkillScreen below To Do in future sprints
def printSkillFromList(skillName):
    skillIndex = None
    for i, skill in enumerate(SKILL_LIST):
        if skill["name"] == skillName:
            skillIndex = i
            break
    if skillIndex == None:
        return -1
    print("*** Learn {} ***".format(SKILL_LIST[skillIndex]["name"]))
    print(SKILL_LIST[skillIndex]["desc"])
    input("")
    return
