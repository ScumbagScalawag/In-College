from common_utils.types.user import User
from main import printInitialScreen
from pages.initial_screen import printInitialScreen, initialScreenOptionsList, testimonialOutputList
from pages.important_links import importantLinksOptionsList
from pages.useful_links import usefulLinksOptionsList
from pages.friend_search import friendSearchOptionList
import pytest
from common_utils.types.user_database import UserDatabase
from tests.shared import threeAccounts, singleUser
from common_utils.messages import alreadyLoggedIn, anyButtonToContinueMessage, invalidInput

# TODO: Possibly combine into *testimonialOutputList, *initialScreenOptionsList, *XoptionsList for testing. Xoptions list is not uniformly implemented so would need to be implemented and then imported to work.
# - Lots of imports, + Simpler Code


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["anything", "1"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                alreadyLoggedIn("Please log out and log back in to change accounts"),
                anyButtonToContinueMessage(),
            ],
            [],
        ),
        (
            ["anything", "2"],  # New account screen
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                alreadyLoggedIn("Please log out to create another account."),
            ],
            [],
        ),
        (
            ["anything", "3"],  # Search for friend user
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                *friendSearchOptionList,
            ],
            [],
        ),
        (
            ["anything", "4"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                *usefulLinksOptionsList,
            ],
            [],
        ),
        (
            ["anything", "5"],
            [*testimonialOutputList, *initialScreenOptionsList, *importantLinksOptionsList],
            [],
        ),
        (
            ["anything", "X"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                "Exiting InCollege",
            ],
            None,
        ),
        (
            ["anything", "FoamEarplugs"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                invalidInput("1, 2, 3, 4, 5, 6, or X"),
            ],
            [],
        ),
    ],
    ids=[
        "1-Login",
        "2-CreateNewAccount",
        "3-FindSomeone",
        "4-UsefulLinks",
        "5-ImportantLinks",
        "X-Close",
        "InvalidSelection",
    ],
)
def testPrintInitial(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    userDB = UserDatabase([])
    # Load 3 accounts to Json
    userDB.addUserDictList(threeAccounts)
    testUser = User.dictToUser(singleUser)

    try:
        assert printInitialScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
