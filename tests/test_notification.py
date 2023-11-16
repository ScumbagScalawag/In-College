import pytest

from common_utils.types.user_database import UserDatabase
from tests.shared import JSON_USERS_FP, fourAccounts


def tempFunction():
    return


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["", ""],  # mock input
            [
                "",  # responses
                "",
            ],
            None,  # expected return
        ),
        (
            ["1st input", "2nd input"],
            [
                "",
                "",
            ],
            None,
        ),
        (
            [""],
            [
                "",
            ],
            None,
        ),
    ],
    ids=[
        "NotLoggedIn",
        "JobsNotification",
        "ProfileNotification",
    ],
)
def testNotifications(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert tempFunction() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
