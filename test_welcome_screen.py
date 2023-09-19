import pytest
from main import printInitialScreen

def testPrintInitialScreen(monkeypatch, capfd):
    input_generator = iter(["6"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))

    try:
        printInitialScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    main_menu = (
        """*** Welcome to InCollege ***\n
        1 - Login as existing user\n
        2 - Create a new InCollege account\n"""
    )
    assert main_menu in captured.out
