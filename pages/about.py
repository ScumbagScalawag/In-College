from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printAboutScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(aboutOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


aboutOptions = [
    "*** About ***",  # added in order to test important_links.py properly
    underConstructionMessage(),
]
