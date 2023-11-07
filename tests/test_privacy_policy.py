import pytest
from pages.privacy_policy import printPrivacyPolicyScreen, privacyPolicyOptions
from common_utils.messages import anyButtonToContinueMessage


def testPrintPrivacyPolicyScreen(monkeypatch, capfd):
    mock_input = ["1"]
    responses = [
        *privacyPolicyOptions,
        "You must be logged in to access guest controls.\n",
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printPrivacyPolicyScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


def testPrintPrivacyPolicyScreen_InvalidInput(monkeypatch, capfd):
    mock_input = ["2", "X"]
    responses = [
        *privacyPolicyOptions,
        'Invalid selection please input "1" or "X"',
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printPrivacyPolicyScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
