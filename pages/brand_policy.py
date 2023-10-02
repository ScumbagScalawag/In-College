from typing import Optional
from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printBrandPolicyScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(brandPolicyOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


brandPolicyOptions = [underConstructionMessage()]
