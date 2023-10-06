from typing import Optional

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printCopyrightPolicyScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(copyrightPolicyOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


copyrightPolicyOptions = [
    "*** Copyright Policy ***",  # added in order to test important_links.py properly
    """All content on this application, including text, images, and multimedia, is protected 
by copyright laws. Users are prohibited from reproducing, distributing, or modifying any 
part of this content without explicit permission. Requests for content usage should be 
submitted in writing to [Your Contact Email/URL]. We take copyright infringement seriously 
and will respond promptly to valid infringement notices. """,
]
