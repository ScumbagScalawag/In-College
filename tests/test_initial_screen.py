from main import printInitialScreen
from pages.initial_screen import printInitialScreen, initialScreenOptionsList, testimonialOutputList
import pytest

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
                "*** Find A Friend ***",  # TODO: Later down the line. Simplify other functions to use similar logic as friendSearchOptionList, might clutter up testing imports though
                "Search for someone you know on InCollege",
            ],
            [],
        ),
        (
            ["anything", "4"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                "*** Useful Links ***",  # TODO: *usefulLinksOptionsList
            ],
            [],
        ),
        (
            ["anything", "5"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                "*** InCollege Important Links ***",  # TODO: *importantLinksOptionsList
            ],
            [],
        ),
        (
            ["anything", "X"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                "Exiting InCollege",
            ],
            0,
        ),
        (
            ["anything", "FoamEarplugs"],
            [
                *testimonialOutputList,
                *initialScreenOptionsList,
                'Invalid selection please input "1" or "2"',
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

    try:
        assert printInitialScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
