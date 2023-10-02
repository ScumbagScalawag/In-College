from typing import Optional

from common_utils.types.user import User
from common_utils.messages import anyButtonToContinueMessage, invalidInput, returnToPreviousMenuMessage
from common_utils.utils import clearScreen, printOptionList

from pages.accessibility import printAccessibilityScreen
from pages.brand_policy import printBrandPolicyScreen
from pages.cookie_policy import printCookiePolicyScreen
from pages.copyright_policy import printCopyrightPolicyScreen
from pages.guest_controls import printGuestControlsScreen
from pages.languages import printLanguagesScreen
from pages.privacy_policy import printPrivacyPolicyScreen
from pages.copyright_notice import printCopyrightNoticeScreen
from pages.about import printAboutScreen
from pages.user_agreement import printUserAgreementScreen


# opens important links menu
def printImportantLinkScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(importantLinksOptionsList)
        userInput = input("")

        if userInput == "1":
            currentUser = printCopyrightNoticeScreen(currentUser)
            continue
        elif userInput == "2":
            currentUser = printAboutScreen(currentUser)
            continue
        elif userInput == "3":
            currentUser = printAccessibilityScreen(currentUser)
            continue
        elif userInput == "4":
            currentUser = printUserAgreementScreen(currentUser)
            continue
        elif userInput == "5":
            currentUser = printPrivacyPolicyScreen(currentUser)
            continue
        elif userInput == "6":
            currentUser = printCookiePolicyScreen(currentUser)
            continue
        elif userInput == "7":
            currentUser = printCopyrightPolicyScreen(currentUser)
            continue
        elif userInput == "8":
            currentUser = printBrandPolicyScreen(currentUser)
            continue
        elif userInput == "9":
            currentUser = printGuestControlsScreen(currentUser)
            continue
        elif userInput == "10":
            currentUser = printLanguagesScreen(currentUser)
            continue
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or X"))
            print(anyButtonToContinueMessage())
            input("")
    return currentUser


importantLinksOptionsList = [
    "*** InCollege Important Links ***",
    "1 - A Copyright Notice",
    "2 - About",
    "3 - Accessibility",
    "4 - User Agreement",
    "5 - Privacy Policy",
    "6 - Cookie Policy",
    "7 - Copyright Policy",
    "8 - Brand Policy",
    "9 - Guest Controls",
    "10 - Languages",
    returnToPreviousMenuMessage(),
]
