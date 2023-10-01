from common_utils.messages import returnToPreviousMenuMessage
from common_utils.utils import clearScreen, printOptionList
from pages.guest_controls import printGuestControlsPage


def printPrivacyPolicyPage(currentUser=None):
    while True:
        # clearScreen()
        print("-----printPrivacyPolicyPage")
        printOptionList(privacyPolicyOptions)

        userInput = input("")
        if userInput == "1":
            printGuestControlsPage()
        elif userInput.upper() == "X":
            break
        else:
            print('Invalid selection please input "1" or "X"')
    return


privacyPolicyOptions = [
    "*** Privacy Policy ***",
    """Here at InCollege we value your privacy. User data is always collected 
and analyzed anonymously and is always encrypted. We strive to make all 
notifications and targeted advertizing features as beneficial as possible
for our users. Should you want to opt out of some of the default settings,
see the below menu.\n""",
    "1 - Guest Controls",
    returnToPreviousMenuMessage(),
]
