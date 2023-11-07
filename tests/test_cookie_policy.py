from pages.cookie_policy import printCookiePolicyScreen, cookiePolicyOptions
from common_utils.messages import anyButtonToContinueMessage


def test_printBrandPolicyScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *cookiePolicyOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printCookiePolicyScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
