from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printCookiePolicyScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(cookiePolicyOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


cookiePolicyOptions = [
    "*** Cookie Policy ***",  # added in order to test important_links.py properly
    underConstructionMessage(),
]
