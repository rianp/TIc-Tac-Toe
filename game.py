"""
This module contains the `game` function that creates any
necessary objects and calls functions to execute the program's logic.
"""
from console import *
from board import *
from score import *
from player import *
from turn import *
from validation import *


class Game:
    """ Responsible for managing the game flow. """
    def __init__(self):
        self._board = Board()
        self._player_1 = Player("1", "x")
        self._player_2 = Player("2", "o")
        self._players = (self._player_1, self._player_2)
        self._turn = Turn()

    def play(self):
        """ Creates any necessary objects and calls functions to execute the program's logic. """
        Console.print_string("Hello friend, welcome to Tic-Tac-Toe!")
        self.display_instructions()

        while True:
            Console.print_string(str(self._board))
            user_input = self.prompt_user_input()

            current_player = self._players[self._turn.get_current_turn() - 1]
            self._board.update_board(current_player.get_player_mark(), user_input)

            game_status = self.check_game_status()

            if game_status == "Tie":
                Console.print_string("Eek! Looks like it's a tie friends. Goodbye.")
                break

            if game_status:
                Console.print_string\
                    (f"OMG! Congratulations Player {self._turn.get_current_turn()}, You won!")
                break

            self._turn.change_turn()

    @staticmethod
    def display_instructions():
        """ Displays instructions of the game. """
        message = """
*------------------------------------------------------------*
* Here are the instructions to the game!                     *
*------------------------------------------------------------*
* 1. there are two players in the game (X and O)             *
* 2. a game has nine fields in a 3x3 grid                    *
* 3. a player can take a field if not already taken          *
* 4. players take turns taking fields until the game is over *
* 5. a game is over when:                                    *
*   - all fields in a row are taken by a player              *
*   - all fields in a column are taken by a player           *
*   - all fields in a diagonal are taken by a player         *
*   - all fields are taken                                   *
*------------------------------------------------------------* 
        """
        Console.print_string(message)

    def prompt_user_input(self):
        """ Prompts user for input. """
        user_input = Console.prompt_input\
            (f'\nHi Player {self._turn.get_current_turn()}! Enter a value please: ')
        validated_input = self.validate_user_input(user_input)
        return validated_input

    def validate_user_input(self, user_input):
        """ Validates user input. """
        validator = Validation()
        while not validator.validate_selection(user_input, self._board.get_board()):
            Console.print_string("Oops! This is an invalid menu choice. ")
            user_input = Console.prompt_input("\nLet's try that again! Enter a value please: ")
        return user_input

    def check_game_status(self):
        """ Checks game status. """
        return Score.get_game_status(self._board.get_board())
