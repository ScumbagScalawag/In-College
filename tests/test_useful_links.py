import pytest
from pages.useful_links import printUsefulLinkScreen, usefulLinksOptionsList

# underConstructionMessage = "under construction, input anything to return" #
from common_utils.messages import underConstructionMessage, invalidInput


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # General
            [
                *usefulLinksOptionsList,
                "*** General ***",  # Some weird things going on in there, might need more work later
            ],
            [],
        ),
        (
            ["2"],  # BrowseInCollege
            [
                *usefulLinksOptionsList,
                "*** Browse InCollege ***",
            ],
            [],
        ),
        (
            ["3"],  # Business Solutions
            [
                *usefulLinksOptionsList,
                "*** Business Solutions ***",
            ],
            [],
        ),
        (
            ["4"],  # Directories
            [
                *usefulLinksOptionsList,
                "*** Directories ***",
            ],
            [],
        ),
        (
            ["X"],  # Return
            [
                *usefulLinksOptionsList,
            ],
            None,  # We are currentUser=None
        ),
        (
            ["FoamEarplugs"],  # Invalid Input
            [
                *usefulLinksOptionsList,
                invalidInput("1, 2, 3, 4 or X"),
                anyButtonToContinueMessage(),
            ],
            [],
        ),
    ],
    ids=[
        "1-General",
        "2-BrowseInCollege",
        "3-BusinessSolutions",
        "4-Directories",
        "X-Return",
        "TODO: InvalidSelection",
    ],
)
def testPrintUsefulLinkScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printUsefulLinkScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
