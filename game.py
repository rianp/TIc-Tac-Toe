from console import *
from board import *
from score import *
from player import *
from turn import *
from validation import *


class Game:
    def __init__(self):
        self._board = Board()
        self._player_1 = Player("1", "x")
        self._player_2 = Player("2", "o")
        self._players = (self._player_1, self._player_2)
        self._turn = Turn()

    def play(self):
        Console().print_string("Hello friend, welcome to Tic-Tac-Toe!")
        self.display_instructions()

        while True:
            Console().print_string(str(self._board))
            user_input = self.prompt_user_input(f'\nHi Player {self._turn.get_current_turn()}! Enter a value please: ')

            current_player = self._players[self._turn.get_current_turn() - 1]
            self._board.update_board(current_player.get_mark(), user_input)

            game_status = self.check_game_status()

            if game_status == "Tie":
                Console().print_string("Eek! Looks like it's a tie friends. Goodbye.")
                break

            if game_status:
                Console().print_string\
                    (f"OMG! Congratulations Player {self._turn.get_current_turn()}, You won!")
                break

            self._turn.change_turn()

    @staticmethod
    def display_instructions():
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
        Console().print_string(message)

    def prompt_user_input(self, string):
        user_input = Console().prompt_input(string)
        validated_input = self.validate_user_input(user_input)
        return validated_input

    def validate_user_input(self, user_input):
        string = "\nIt's okay though! We'll try again! Enter a value please: "
        validator = Validator()
        while True:
            if not validator.is_valid_integer(user_input):
                Console().print_string("Eek! That's not even a number! ")
            elif not validator.is_in_range(int(user_input), self._board.get_board_range()):
                Console().print_string("Whoa friend! This is outa bounds! ")
            elif not validator.is_on_board(int(user_input), self._board.get_board()):
                Console().print_string("Rats! Your opponent already snagged this one! ")
            else:
                return int(user_input)
            user_input = Console().prompt_input(string)

    def check_game_status(self):
        return Score.get_game_status(self._board.get_board())
