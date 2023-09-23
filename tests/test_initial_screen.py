from main import printInitialScreen
from pages.initial_screen import printInitialScreen
import pytest
@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["anything", "1"],
            [
                "*** Welcome to InCollege ***",
                "Here is a story from one of our users:",
                "1 - Login as existing user",
                "2 - Create a new InCollege account",
                "3 - Find InCollege users",
                "X - Close Program",
                "Login to InCollege",
                "Username: ",
            ],
            [],
        ),
        (
            ["anything", "2"],  # New account screen
            [
                "*** Welcome to InCollege ***",
                "Here is a story from one of our users:",
                "1 - Login as existing user",
                "2 - Create a new InCollege account",
                "3 - Find InCollege users",
                "X - Close Program",
            ],
            [],
        ),
        (
            ["anything", "3"],  # Search for friend user
            [
                "*** Welcome to InCollege ***",
                "Here is a story from one of our users:",
                "1 - Login as existing user",
                "2 - Create a new InCollege account",
                "3 - Find InCollege users",
                "X - Close Program",
                "*** Find A Friend ***",
                "Search for someone you know on InCollege",
            ],
            [],
        ),
        (
            ["anything", "X"],
            [
                "*** Welcome to InCollege ***",
                "Here is a story from one of our users:",
                "1 - Login as existing user",
                "2 - Create a new InCollege account",
                "3 - Find InCollege users",
                "X - Close Program",
                "Exiting InCollege",
            ],
            [0],
        ),
        (
            ["anything", "FoamEarplugs"],
            [
                "*** Welcome to InCollege ***",
                "1 - Login as existing user",
                "2 - Create a new InCollege account",
                "3 - Find InCollege users",
                "X - Close Program",
                'Invalid selection please input "1" or "2"',
            ],
            [],
        ),
    ],
    ids=["1-Login", "2-CreateNewAccount", "3-FindSomeone", "X-Close", "InvalidSelection"],
)
def testPrintInitial(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        printInitialScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
