import random


class NumberGuessingGame:
    """Number guessing game with difficulty levels and scoring."""

    DIFFICULTIES = {
        "easy": {"max_number": 50, "attempts": 10},
        "medium": {"max_number": 100, "attempts": 7},
        "hard": {"max_number": 200, "attempts": 5},
    }

    def __init__(self, difficulty="medium"):
        if difficulty not in self.DIFFICULTIES:
            raise ValueError("Invalid difficulty level.")

        self.difficulty = difficulty
        self.max_number = self.DIFFICULTIES[difficulty]["max_number"]
        self.max_attempts = self.DIFFICULTIES[difficulty]["attempts"]
        self.secret_number = random.randint(1, self.max_number)
        self.attempts_used = 0
        self.score = 0
        self.game_over = False

    def make_guess(self, guess):
        """Process a player's guess and return a result."""
        if self.game_over:
            return "Game over. Start a new game."

        if not isinstance(guess, int):
            return "Please enter a valid number."

        if guess < 1 or guess > self.max_number:
            return f"Enter a number between 1 and {self.max_number}."

        self.attempts_used += 1

        if guess == self.secret_number:
            self.score = (self.max_attempts - self.attempts_used + 1) * 10
            self.game_over = True
            return f"Correct! You scored {self.score} points."

        if self.attempts_used >= self.max_attempts:
            self.game_over = True
            return (
                f"Game over! The correct number was "
                f"{self.secret_number}."
            )

        if guess < self.secret_number:
            return "Too low!"

        return "Too high!"

    def attempts_remaining(self):
        """Return the number of attempts remaining."""
        return self.max_attempts - self.attempts_used

    def reset(self):
        """Reset the game with a new secret number."""
        self.secret_number = random.randint(1, self.max_number)
        self.attempts_used = 0
        self.score = 0
        self.game_over = False