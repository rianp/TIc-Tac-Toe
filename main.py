"""
The Tic-Tac-Toe game console interface.

This module defines a `Console` class representing a console interface for the
Tic-Tac-Toe game. It also includes a `main` function that creates a `Console`
object and calls its `greeting` method to display a welcome message to the user.
"""

class Console:
    """ A class representing a console interface for Tic-Tac-Toe game. """
    def greeting(self):
        """  Returns a welcome message to the user. """
        return "Welcome to Tic-Tac-Toe."


def main():
    """ Creates any necessary objects and calls functions to execute the program's logic. """
    welcome = Console()
    print(welcome.greeting())


if __name__ == "__main__":
    main()
