from typing import Optional

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printCookiePolicyScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(cookiePolicyOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


cookiePolicyOptions = [
    "*** Cookie Policy ***",  # added in order to test important_links.py properly
    "This application uses cookies to enhance your user experience.",
    "By using the application, you consent to the use of cookies for this purpose, as agreed upon in the user agreement."
    "No user-configurable options for managing cookies are available at this time",
]
