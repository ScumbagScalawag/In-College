from pages.copyright_policy import copyrightPolicyOptions, printCopyrightPolicyScreen
from common_utils.messages import anyButtonToContinueMessage
import pytest


def testPrintCopyrightPolicyScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *copyrightPolicyOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printCopyrightPolicyScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
