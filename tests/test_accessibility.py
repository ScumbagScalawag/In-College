import pytest
from common_utils.messages import anyButtonToContinueMessage
from pages.accessibility import printAccessibilityScreen, accessibilityOptions


def test_printAccessibilityScreen(monkeypatch, capfd):
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
