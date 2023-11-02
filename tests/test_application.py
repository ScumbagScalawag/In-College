import pytest
from pages.application import applyToJob, checkDate, personalApplicationList, notAppliedList
from tests.shared import singleUser

def test_applyToJob(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *accessibilityOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printAccessibilityScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


@pytest.mark.parametrize(
    "mock_input,jobIndex,testUser,responses,expectedReturn",
    [
        (
            [""],  # mock input
            0,
            None,  # test user
            [
                "You must be logged in to create a Job.",
                anyButtonToContinueMessage(),
            ],  # responses
            None,  # expected return
        ),
        (

        ),
    ],
    ids=["None User", "2-FriendSearch", "3-Skill", "X-Exit", "Invalid Selection"],
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
