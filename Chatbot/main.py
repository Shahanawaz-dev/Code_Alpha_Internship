from chatbot import Chatbot


def get_user_input():
    """Get valid input from the user."""
    while True:
        user_input = input("You: ").strip()

        if user_input:
            return user_input

        print("PyBot: Please enter a message.")


def main():
    """Run the chatbot application."""
    bot = Chatbot("PyBot")

    print("=" * 40)
    print("           Welcome to PyBot")
    print("=" * 40)
    print("Type 'help' to see what I can do.")
    print("Type 'history' to view the conversation.")
    print("Type 'bye' to exit.")
    print()

    while True:
        try:
            user_input = get_user_input()

            response = bot.respond(user_input)

            print(f"PyBot: {response}")

            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                break

        except KeyboardInterrupt:
            print("\nPyBot: Goodbye!")
            break

        except Exception as error:
            print(f"PyBot: An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()