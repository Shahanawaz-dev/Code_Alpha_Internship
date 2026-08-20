from chatbot import Chatbot


def test_greeting():
    bot = Chatbot()

    response = bot.respond("hello")

    assert "Hello" in response


def test_name():
    bot = Chatbot()

    response = bot.respond("what is your name")

    assert "PyBot" in response


def test_python_question():
    bot = Chatbot()

    response = bot.respond("tell me about python")

    assert "Python" in response


def test_empty_input():
    bot = Chatbot()

    response = bot.respond("")

    assert response == "Please enter a message."


def test_unknown_input():
    bot = Chatbot()

    response = bot.respond("something random")

    assert "not sure" in response


def test_conversation_history():
    bot = Chatbot()

    bot.respond("hello")

    history = bot.get_history()

    assert "hello" in history
    assert "Hello" in history


def test_clear_history():
    bot = Chatbot()

    bot.respond("hello")
    bot.clear_history()

    assert bot.conversation_history == []