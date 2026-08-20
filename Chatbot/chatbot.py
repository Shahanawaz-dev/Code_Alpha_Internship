class Chatbot:
    """A simple rule-based chatbot."""

    def __init__(self, name="PyBot"):
        self.name = name
        self.conversation_history = []

    def respond(self, user_input):
        """Generate a response based on user input."""
        user_input = user_input.strip().lower()

        if not user_input:
            return "Please enter a message."

        if user_input in ["hello", "hi", "hey"]:
            response = f"Hello! I'm {self.name}. How can I help you?"

        elif "your name" in user_input:
            response = f"My name is {self.name}."

        elif "how are you" in user_input:
            response = "I'm doing great! Thanks for asking."

        elif "python" in user_input:
            response = (
                "Python is a powerful programming language used "
                "in web development, automation, data science, and AI."
            )

        elif "help" in user_input:
            response = (
                "You can ask me about my name, Python, or how I am. "
                "You can also use the 'history' command."
            )

        elif user_input == "history":
            response = self.get_history()

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            response = "Goodbye! Have a great day."

        else:
            response = (
                "I'm not sure how to respond to that. "
                "Try typing 'help' to see what I can do."
            )

        self.conversation_history.append(("User", user_input))
        self.conversation_history.append((self.name, response))

        return response

    def get_history(self):
        """Return the conversation history."""
        if not self.conversation_history:
            return "There is no conversation history yet."

        history = ["Conversation History:"]

        for speaker, message in self.conversation_history:
            history.append(f"{speaker}: {message}")

        return "\n".join(history)

    def clear_history(self):
        """Clear the stored conversation history."""
        self.conversation_history.clear()