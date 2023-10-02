from typing import Optional
from common_utils.types.user import User
from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.utils import printOptionList


def printAccessibilityScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(accessibilityOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


accessibilityOptions = [underConstructionMessage()]
