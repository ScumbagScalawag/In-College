from common_utils.messages import anyButtonToContinueMessage
from pages.user_agreement import printUserAgreementScreen, userAgreementOptions
import pytest


def test_printAboutScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *userAgreementOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printUserAgreementScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
