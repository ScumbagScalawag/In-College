from main import printInitialScreen
from pages.initial_screen import printInitialScreen

def testPrintInitialScreen(monkeypatch, capfd):
    input_generator = iter(["2"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

    try:
        printInitialScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()

    title = "*** Welcome to InCollege ***"
    existingUser = "1 - Login as existing user"
    newAccount = "2 - Create a new InCollege account"

    assert title in captured.out
    assert existingUser in captured.out
    assert newAccount in captured.out
