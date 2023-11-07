import pytest
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from pages.guest_controls import (
    printGuestControlsScreen,
    guestControlsList,
    notificationSettingsError,
    unsubscribeMessage,
    subscribeMessage,
    toggleUserEmailSubscription,
    toggleUserSmsSubscription,
    toggleUserTargetedAds,
)
from tests.shared import singleUser, fourAccounts
from common_utils.messages import invalidInput


@pytest.mark.parametrize(
    "mock_input,responses",
    [
        (
            ["1"],  # Email Subscription
            [
                *guestControlsList,
                *unsubscribeMessage,
            ],
        ),
        (
            ["2"],  # SMS Subscription
            [
                *guestControlsList,
                *unsubscribeMessage,
            ],
        ),
        (
            ["3"],  # Targeted Ads
            [
                *guestControlsList,
                *unsubscribeMessage,
            ],
        ),
        (
            ["X"],  # Return to Previous Menu
            [
                *guestControlsList,
            ],
        ),
        (
            ["4"],  # Invalid Input
            [*guestControlsList, invalidInput('"1" or "2" or "3" or "X"')],
        ),
    ],
    ids=[
        "1-Email Subscription",
        "2-SMS Subscription",
        "3-Targeted Ads",
        "X-Return to Previous Menu",
        "Invalid Input",
    ],
)
def testPrintGuestControlsScreen(monkeypatch, capfd, mock_input, responses):
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    testUser = User.dictToUser(singleUser)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printGuestControlsScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for response in responses:
        assert response in captured.out


def testToggleUserEmailSubscription(monkeypatch, capfd):
    testUser = User.dictToUser(singleUser)
    startingBool = testUser.emailSub
    finalBool = not startingBool
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    mock_input = [""]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert testUser.emailSub == startingBool
        assert toggleUserEmailSubscription(testUser) == testUser
        assert testUser.emailSub == finalBool
    except StopIteration:
        pass


def testToggleUserSmsSubscription(monkeypatch, capfd):
    testUser = User.dictToUser(singleUser)
    startingBool = testUser.smsSub
    finalBool = not startingBool
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    mock_input = [""]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert testUser.smsSub == startingBool
        assert toggleUserSmsSubscription(testUser) == testUser
        assert testUser.smsSub == finalBool
    except StopIteration:
        pass


def testToggleUserTargetedAds(monkeypatch, capfd):
    testUser = User.dictToUser(singleUser)
    startingBool = testUser.adSub
    finalBool = not startingBool
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    mock_input = [""]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert testUser.adSub == startingBool
        assert toggleUserTargetedAds(testUser) == testUser
        assert testUser.adSub == finalBool
    except StopIteration:
        pass
