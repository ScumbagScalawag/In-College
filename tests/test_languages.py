from pages.languages import printLanguagesScreen, languageLoggedOutOptions, languageLoggedInOptions
from common_utils.messages import anyButtonToContinueMessage, invalidInput
from tests.shared import singleUser
from common_utils.types.user import User


def test_printLanguagesScreen_LoggedOut(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *languageLoggedOutOptions,
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printLanguagesScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


def test_printLanguagesScreen_LoggedIn(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *languageLoggedInOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = User.dictToUser(singleUser)
    try:
        assert printLanguagesScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


def test_printLanguagesScreen_LoggedIn_InvalidInput(monkeypatch, capfd):
    mock_input = [
        "A",
        "X",
        "X",
    ]
    responses = [
        *languageLoggedInOptions,
        invalidInput("1, 2, or X"),
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = User.dictToUser(singleUser)
    try:
        assert printLanguagesScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
