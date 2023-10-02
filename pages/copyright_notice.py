from typing import Optional
from common_utils.types.user import User
from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.utils import printOptionList


def printCopyrightNoticeScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(copyrightNoticeOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


copyrightNoticeOptions = [underConstructionMessage()]
