from typing import Optional

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printAboutScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(aboutOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


aboutOptions = [
    "*** About ***",  # added in order to test important_links.py properly
    "InCollege is a platform designed to bring students together and help them begin their career.",
    "We are dedicated to providing valuable connections between students to foster life-long professional connections.",
    "Our team is passionate about providing the best platform for connecting students.",
    "Thank you for choosing InCollege!",
]
