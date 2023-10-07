from typing import Dict, Optional

from common_utils.types.user import User


def underConstructionMessage():
    return "under construction, input anything to return"


def returnToPreviousMenuMessage():
    return "X - Return to previous menu"


# TODO: Inherently make this print and then wait for input with 'input("")'
def anyButtonToContinueMessage():
    return "Press any button to continue..."


def invalidInput(validInputCSV):
    return "Invalid selection please input " + validInputCSV


def convertDictKeysToValidInputString(dictionary: Dict):
    # Convert numerical options to text in array
    keyText = [str(key) for key in dictionary.keys()]
    # This is assuming each option list returns back a page
    keyText.append("or X")

    # Create a comma-separated string of options
    optionsStringCSV = ", ".join(keyText)
    return optionsStringCSV

def invalidInputPressToContinue(validInputCSV: str):
    print(invalidInput(validInputCSV))
    print(anyButtonToContinueMessage())
    input("")

def mustBeLoggedIn():
    return "You must be logged in to view this page"


def alreadyLoggedIn(additionalInfo):
    return "You are already logged in. " + additionalInfo


# Must pass in currentUser. Pass contentText for page-specific info: contentText="guest controls"
def isLoggedIn(currentUser: Optional[User], contentText: str) -> bool:
    # if not logged in (currentUser == None)
    if not isinstance(currentUser, User):
        if contentText:
            print(f"You must be logged in to access {contentText}.\n")
        else:
            print("You must be logged in to access this page.\n")
        print(anyButtonToContinueMessage())
        input("")
        return False

    else:
        return True

def findFriendsRecommendation():
    return "Use InCollege\'s \"Find Friends\" feature to expand your network!"
