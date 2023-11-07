from common_utils.messages import anyButtonToContinueMessage
from pages.about import printAboutScreen, aboutOptions
import pytest

def test_printAboutScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *aboutOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printAboutScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
