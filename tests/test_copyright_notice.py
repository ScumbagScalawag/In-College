from pages.copyright_notice import printCopyrightNoticeScreen, copyrightNoticeOptions
from common_utils.messages import anyButtonToContinueMessage
from pages import copyright_notice
import pytest


def testPrintCopyrightNoticeScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *copyrightNoticeOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert copyright_notice.printCopyrightNoticeScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
