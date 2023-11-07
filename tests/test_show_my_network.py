import pytest
from pages.show_my_network import printShowMyNetworkScreen, showMyNetworkOptions
from common_utils.types.user import User
from tests.shared import singleUser


@pytest.mark.parametrize(
    "mock_input,responses",
    [
        (
            ["1", "Foam Earplugs"],
            [
                *showMyNetworkOptions,
                "*** Friends ***",
            ],
        ),
        (
            ["2", "Foam Earplugs"],
            [
                *showMyNetworkOptions,
                "*** Outgoing Friend Requests ***",
            ],
        ),
        (
            ["3", "Foam Earplugs"],
            [
                *showMyNetworkOptions,
                "*** Profile of Noah McIvor ***",
            ],
        ),
        (
            ["4", "Foam Earplugs"],
            [
                *showMyNetworkOptions,
                "*** Edit Profile ***",
            ],
        ),
        (
            ["X"],
            [
                *showMyNetworkOptions,
            ],
        ),
        (
            ["Foam Earplugs"],
            [
                *showMyNetworkOptions,
                "Invalid selection please input 1, 2, 3, 4, or X",
            ],
        ),
    ],
    ids=[
        "1-Friends",
        "2-Outgoing Friend Requests",
        "3-Profile",
        "4-Edit Profile",
        "X-Exit",
        "Invalid Input",
    ],
)
def testPrintShowMyNetworkScreen(mock_input, responses, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = User.dictToUser(singleUser)
    try:
        assert printShowMyNetworkScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for response in responses:
        assert response in captured.out
