from game import NumberGuessingGame


def choose_difficulty():
    """Ask the player to choose a difficulty level."""
    while True:
        print("\nChoose difficulty:")
        print("1. Easy   (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard   (1-200, 5 attempts)")

        choice = input("Enter choice (1-3): ").strip()

        difficulties = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }

        if choice in difficulties:
            return difficulties[choice]

        print("Invalid choice. Please select 1, 2, or 3.")


def get_guess(max_number):
    """Get a valid numerical guess from the player."""
    while True:
        user_input = input(
            f"Enter your guess (1-{max_number}): "
        ).strip()

        try:
            guess = int(user_input)

            if 1 <= guess <= max_number:
                return guess

            print(f"Please enter a number between 1 and {max_number}.")

        except ValueError:
            print("Please enter a valid whole number.")


def play_game():
    """Run one complete game."""
    difficulty = choose_difficulty()
    game = NumberGuessingGame(difficulty)

    print(f"\nYou selected {difficulty.upper()} mode.")
    print(f"Guess a number between 1 and {game.max_number}.")
    print(f"You have {game.max_attempts} attempts.")

    while not game.game_over:
        guess = get_guess(game.max_number)
        result = game.make_guess(guess)

        print(f"\n{result}")

        if not game.game_over:
            print(
                f"Attempts remaining: "
                f"{game.attempts_remaining()}"
            )

    print(f"Final score: {game.score}")


def main():
    """Run the game application."""
    print("=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)

    while True:
        play_game()

        choice = input("\nPlay again? (y/n): ").strip().lower()

        if choice != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()