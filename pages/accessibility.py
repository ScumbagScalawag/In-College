from typing import Optional

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printAccessibilityScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(accessibilityOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


accessibilityOptions = [
    "*** Accessibility ***",  # added in order to test important_links.py properly
    "This application is designed with accessibility in mind to ensure a better user experience for all users.",
]
