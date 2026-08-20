from game import NumberGuessingGame


def test_valid_guess_too_low():
    game = NumberGuessingGame("easy")
    game.secret_number = 25

    result = game.make_guess(10)

    assert result == "Too low!"
    assert game.attempts_used == 1


def test_valid_guess_too_high():
    game = NumberGuessingGame("easy")
    game.secret_number = 25

    result = game.make_guess(40)

    assert result == "Too high!"
    assert game.attempts_used == 1


def test_correct_guess():
    game = NumberGuessingGame("easy")
    game.secret_number = 25

    result = game.make_guess(25)

    assert "Correct" in result
    assert game.game_over is True
    assert game.score > 0


def test_invalid_number_range():
    game = NumberGuessingGame("easy")

    result = game.make_guess(100)

    assert "between 1 and 50" in result
    assert game.attempts_used == 0


def test_invalid_data_type():
    game = NumberGuessingGame("easy")

    result = game.make_guess("abc")

    assert result == "Please enter a valid number."


def test_attempts_remaining():
    game = NumberGuessingGame("medium")
    game.secret_number = 50

    game.make_guess(20)

    assert game.attempts_remaining() == 6


def test_reset():
    game = NumberGuessingGame("easy")
    game.secret_number = 25

    game.make_guess(25)
    game.reset()

    assert game.attempts_used == 0
    assert game.score == 0
    assert game.game_over is False