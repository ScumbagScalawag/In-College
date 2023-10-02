from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printUserAgreementScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(userAgreementOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


userAgreementOptions = [
    "*** User Agreement ***",  # added in order to test important_links.py properly
    underConstructionMessage(),
]
