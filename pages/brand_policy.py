from typing import Optional

from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printBrandPolicyScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(brandPolicyOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


brandPolicyOptions = [
    "*** Brand Policy ***",  # added in order to test important_links.py properly
    "The InCollege brand is a valuable asset, symbolizing our commitment to quality.",
    "InCollege branding should be used consistently and appropriately in all contexts.",
    "Unauthorized use, alteration, or misrepresentation of the InCollege brand is strictly prohibited",
]
