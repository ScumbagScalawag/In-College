from typing import Optional

from common_utils.types.user import User


def underConstructionMessage():
    return "under construction, input anything to return"


def returnToPreviousMenuMessage():
    return "X - Return to previous menu"


def anyButtonToContinueMessage():
    return "Press any button to continue..."


def invalidInput(allowedInput):
    return "Invalid selection please input " + allowedInput


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
