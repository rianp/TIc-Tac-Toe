import unittest
from unittest.mock import MagicMock
from game_start import GameStart


class TestGame(unittest.TestCase):
    def setUp(self):
        self.console = MagicMock()
        self.game = GameStart()

    def test_when_game_starts(self):
        self.game.greeting = MagicMock()
        self.game.instructions = MagicMock()

        self.game.start_game()

        with self.subTest('should display greeting'):
            self.game.greeting.assert_called_once()

        with self.subTest('should display instructions'):
            self.game.instructions.assert_called_once()

    def test_greeting(self):
        expected_output = "\n                         ᕙ(Ⓘ‿‿Ⓘ)ᕗ"\
               "\n   <----** Hello friend! Welcome to Tic-Tac-Toe!!! **----> "
        actual_output = self.game.greeting()
        self.assertEqual(actual_output, expected_output)

    def test_display_instructions(self):
        expected_message = """    
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
        self.game.instructions()
        actual_message = self.game.instructions()

        self.assertEqual(actual_message, expected_message)
