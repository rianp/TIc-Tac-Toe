import unittest
from unittest.mock import MagicMock
from game_start import GameStart


class TestGame(unittest.TestCase):
    def setUp(self):
        self.console = MagicMock()
        self.game = GameStart()

    def test_when_game_starts(self):
        self.game.greeting = MagicMock()
        self.game.display_instructions = MagicMock()

        self.game.start_game(self.console)

        with self.subTest('should display greeting'):
            self.game.greeting.assert_called_once_with(self.console)

        with self.subTest('should display instructions'):
            self.game.display_instructions.assert_called_once_with(self.console)

    def test_greeting(self):
        self.game.greeting(self.console)
        self.console.print_string.assert_called_with(
            "\n<--!!!Hello friend, welcome to Tic-Tac-Toe!!!-->"
        )

    def test_display_instructions(self):
        self.game.display_instructions(self.console)
        message = """
*------------------------------------------------------------*
*           Here are the instructions to the game!           *
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
        self.console.print_string.assert_called_with(message)
