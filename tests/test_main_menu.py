import pytest  # needed for pytest
from pages.main_menu import printMainMenu, mainMenuOptionsList
from common_utils.messages import invalidInput


############################
# ADD TEST FOR NETWORK
############################
@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # mock input
            [
                *mainMenuOptionsList,  # responses
                "*** Job Search ***",
            ],
            None,  # expected return
        ),
        (
            ["2"],
            [
                *mainMenuOptionsList,
                "*** Find A Friend ***",
            ],
            None,
        ),
        (
            ["4"],
            [
                *mainMenuOptionsList,
                "*** Learn a skill ***",
            ],
            None,
        ),
        (
            ["X"],
            [
                *mainMenuOptionsList,
                "Exiting InCollege",
            ],
            None,
        ),
        (
            ["Foam Earplugs"],
            [
                *mainMenuOptionsList,
                invalidInput("1, 2, 3, or X"),
            ],
            None,
        ),
    ],
    ids=[
        "1-JobSearch",
        "2-FriendSearch",
        "3-Skill",
        "X-Exit",
        "Invalid Selection",
    ],
)
def testPrintMainMenu(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printMainMenu(None) == None
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
