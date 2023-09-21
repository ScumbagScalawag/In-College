import pytest
from pages.new_user_account import printNewAccountScreen


# @pytest.mark.parametrize(
#     "password_input",
#     [
#         "small",  # Too short
#         "tkskadkkasdasdlsldlas",  # Too long
#         "lowercase123!",  # No capital letter
#         "UPPERCASEONLY!",  # No digit
#         "NoSpecialChars1",  # No special character
#     ],
# )
# def test_invalid_password_criteria(password_input, monkeypatch, capfd):
#     input_generator = iter(["username", password_input, password_input])
#     monkeypatch.setattr("builtins.input", lambda: next(input_generator))
#     try:
#         printNewAccountScreen()
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     error_message = "Password Requirements: minimum of 8 characters, maximum of 12 characters, at least 1 capital letter, at least 1 digit, at least 1 special character"
#     assert error_message in captured.out
