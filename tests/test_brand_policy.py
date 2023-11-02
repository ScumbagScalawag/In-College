from pages.brand_policy import printBrandPolicyScreen, brandPolicyOptions
from common_utils.messages import anyButtonToContinueMessage

def test_printBrandPolicyScreen(monkeypatch, capfd):
    mock_input = [""]
    responses = [
        *brandPolicyOptions,
        anyButtonToContinueMessage(),
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    testUser = None
    try:
        assert printBrandPolicyScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out