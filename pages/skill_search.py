from common_utils.utils import clearScreen


# user has selected to "Learn a skill"
def printSkillScreen():
    clearScreen()
    while True:
        print("*** Learn a skill ***")
        print("1 - Learn how to skate")
        print("2 - Learn how to cook")
        print("3 - Learn how to drive")
        print("4 - Learn how to paint")
        print("5 - Learn how to whistle")
        print("6 - Return to main menu")
        userInput = input()
        if userInput == "1":
            printSkill1Screen()
        elif userInput == "2":
            printSkill2Screen()
        elif userInput == "3":
            printSkill3Screen()
        elif userInput == "4":
            printSkill4Screen()
        elif userInput == "5":
            printSkill5Screen()
        elif userInput == "6":
            break # returns to caller (main menu) when you "exit"
        else:
            print('Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"')

    return


# TODO: make these functions a single generic function  -noah
# Used with printSkillScreen below To Do in future sprints
def printSkill1Screen():
    # TODO: might not need to cls to make the skill viewing a "single page"
    clearScreen()
    print("*** Learn Skating ***")
    print("under construction, input anything to return")
    userInput = input()

    # NOTE: return to caller instead  -noah
    # printSkillScreen()
    return


def printSkill2Screen():
    clearScreen()
    print("*** Learn Cooking ***")
    print("under construction, input anything to return")
    userInput = input()
    # printSkillScreen()

    # TODO: return to caller instead  -noah
    # printSkillScreen()
    return


def printSkill3Screen():
    clearScreen()
    print("*** Learn Driving ***")
    print("under construction, input anything to return")
    userInput = input()
    # printSkillScreen()

    # TODO: return to caller instead  -noah
    # printSkillScreen()
    return


def printSkill4Screen():
    clearScreen()
    print("*** Learn Painting ***")
    print("under construction, input anything to return")
    userInput = input()
    # printSkillScreen()

    # TODO: return to caller instead  -noah
    # printSkillScreen()
    return


def printSkill5Screen():
    clearScreen()
    print("*** Learn Whistling ***")
    print("under construction, input anything to return")
    userInput = input()
    # printSkillScreen()

    # TODO: return to caller instead  -noah
    # printSkillScreen()
    return
