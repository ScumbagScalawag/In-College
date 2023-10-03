from main import printInitialScreen
from pages.initial_screen import printInitialScreen, initialScreenOptionsList, testimonialOutputList
from pages.important_links import importantLinksOptionsList
from pages.useful_links import usefulLinksOptionsList
from pages.friend_search import friendSearchOptionList
import pytest
from common_utils.types.user_database import UserDatabase
from tests.shared import threeAccounts
from common_utils.messages import invalidInput
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
                "Login to InCollege",
                "Username: ",
            ],
            [],
        ),
        (
            ["anything", "2"],  # New account screen
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                "*** Create a new user account ***",
                "Username: ",
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
    try:
        assert printInitialScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
