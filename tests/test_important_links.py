import pytest

underConstructionMessage = "under construction, input anything to return"  #
from common_utils.types.user_database import UserDatabase
from pages.important_links import importantLinksOptionsList, printImportantLinkScreen
from tests.shared import threeAccounts


def tempFunction():  # Temp function is placeholder for function to be imported from test file
    return


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # Copyright Notice
            [
                *importantLinksOptionsList,
                "*** Copyright Notice ***",
            ],
            [],
        ),
        (
            ["2"],  # About
            [
                *importantLinksOptionsList,
                "*** About ***",
            ],
            [],
        ),
        (
            ["3"],  # Accessibiltiy
            [
                *importantLinksOptionsList,
                "*** Accessibility ***",
            ],
            [],
        ),
        (
            ["4"],  # User Agreement
            [*importantLinksOptionsList, "*** User Agreement ***"],
            [],  # I don't know why the formatting is different for these two
        ),
        (
            ["5"],  # Privacy Policy
            [*importantLinksOptionsList, "*** Privacy Policy ***"],
            [],  # I don't know why the formatting is different for these two
        ),
        (
            ["6"],  # Cookie Policy
            [
                *importantLinksOptionsList,
                "*** Cookie Policy ***",
            ],
            [],
        ),
        (
            ["7"],  # Copyright Policy
            [
                *importantLinksOptionsList,
                "*** Copyright Policy ***",
            ],
            [],
        ),
        (
            ["8"],  # Brand Policy
            [
                *importantLinksOptionsList,
                "*** Brand Policy ***",
            ],
            [],
        ),
        (
            ["9"],  # Guest Controls
            [
                *importantLinksOptionsList,
                "You must be logged in to access guest controls.\n",
            ],
            [],
        ),
        (
            ["10"],  # Languages
            [
                *importantLinksOptionsList,
                "*** Languages ***",
            ],
            [],
        ),
        (
            ["X"],  # Return
            [
                *importantLinksOptionsList,
            ],
            None,  # We are currentUser=None
        ),
        (
            ["FoamEarplugs"],  # Invalid Input
            [
                *importantLinksOptionsList,
            ],
            [],
        ),
    ],
    ids=[
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
        "X - Return",
        "InvalidSelection",
    ],
)
def testPrintUsefulLinkScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    userDB = UserDatabase([])
    # Load 3 accounts to Json
    userDB.addUserDictList(threeAccounts)
    try:
        assert printImportantLinkScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
