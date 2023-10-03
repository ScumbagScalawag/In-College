from typing import Optional

from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.user import User
from common_utils.utils import printOptionList


def printUserAgreementScreen(currentUser: Optional[User] = None) -> Optional[User]:
    printOptionList(userAgreementOptions)
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


userAgreementOptions = [
    "*** User Agreement ***",  # added in order to test important_links.py properly
    "By using this application, you agree to the following terms and conditions:",
    "1. You will use this application responsibly and in accordance with applicable laws.",
    "2. Any data provided to the application is used in accordance with our privacy policy.",
    "3. Cookies are used by the application to enhance user experience and cannot be changed from default values.",
    "\nThese terms are considered agreed upon upon the use of this application.",
    "If you prefer not to agree to these terms, please abstain from using the application",
]
