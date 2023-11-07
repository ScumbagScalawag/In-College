import pytest
from common_utils.messages import anyButtonToContinueMessage, invalidInput
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from pages.important_links import importantLinksOptionsList, printImportantLinkScreen
from tests.shared import fourAccounts, singleUser


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
            [
                *importantLinksOptionsList,
                "*** User Agreement ***",
            ],
            [],  # I don't know why the formatting is different for these two
        ),
        (
            ["5"],  # Privacy Policy
            [
                *importantLinksOptionsList,
                "*** Privacy Policy ***",
            ],
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
                "You must be logged in to access guest controls.",
            ],
            [],
        ),
        (
            ["10"],  # Languages
            [
                *importantLinksOptionsList,
                "*** Languages ***",
                "Please log in to change language settings",
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
                invalidInput("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or X"),
                anyButtonToContinueMessage(),
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
def testPrintImportantLinkScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printImportantLinkScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out

    # # TODO Test Option 9 Not Logged in
    # userDB = UserDatabase([])
    # testUser = User.dictToUser(singleUser)
    # mock_input = [
    #     "9",
    # ]
    # responses = [*importantLinksOptionsList, "You must be logged in to access guest controls.\n"]
    # input_generator = iter(mock_input)
    # monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    # try:
    #     assert printImportantLinkScreen() == testUser
    # except StopIteration:
    #     pass
    # captured = capfd.readouterr()
    # for r in responses:
    #     assert r in captured.out


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["9"],  # Guest Controls
            [
                *importantLinksOptionsList,
                "*** Guest Controls ***",
            ],
            [],
        ),
    ],
    ids=[
        "9 - Guest Controls",
    ],
)
def testPrintImportantLinkScreenLoggedIn(mock_input, responses, expectedReturn, monkeypatch, capfd):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printImportantLinkScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


# # Test to option 9 when logged in
# # TODO: Not sure 100% if this function is correct
# def testPrintImportantLinkScreenLoggedIn(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     testUser = User.dictToUser(singleUser)

#     mock_input = ["anything"]
#     responses = [*importantLinksOptionsList]
#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     try:
#         assert printImportantLinkScreen(testUser) == testUser
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     for r in responses:
#         assert r in captured.out
