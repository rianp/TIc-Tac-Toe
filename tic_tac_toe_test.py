""" This module contains a unit test suite for the application. """

import unittest
from unittest.mock import patch
from game import *
from console import *
from board import *
from player import *
from score import *
from turn import *
from validation import *


class TestGame(unittest.TestCase):
    """ A test suite for the Game class. """
    def setUp(self):
        """ Set up the test game. """
        self.game = Game()

    def test_validate_user_input_valid(self):
        """  Test that validate_user_input() returns the valid user input. """
        self.game._board.update_board('x', '1')
        result = self.game.validate_user_input('2')
        self.assertEqual(result, '2')

    def test_check_game_status_player1_wins_game(self):
        """ Test that check_game_status() returns True when player 1 wins. """
        self.game._board.update_board('x', '1')
        self.game._board.update_board('x', '2')
        self.game._board.update_board('x', '3')
        result = self.game.check_game_status()
        self.assertTrue(result)

    def test_check_game_status_player2_win(self):
        """ Test that check_game_status() returns True when player 2 wins. """
        self.game._board.update_board('o', '1')
        self.game._board.update_board('o', '4')
        self.game._board.update_board('o', '7')
        result = self.game.check_game_status()
        self.assertTrue(result)

    def test_check_game_status_tie(self):
        """ Test that check_game_status() returns 'Tie' when the game ends in a tie. """
        self.game._board.update_board('x', '1')
        self.game._board.update_board('o', '2')
        self.game._board.update_board('x', '3')
        self.game._board.update_board('x', '4')
        self.game._board.update_board('o', '5')
        self.game._board.update_board('o', '7')
        self.game._board.update_board('o', '6')
        self.game._board.update_board('x', '8')
        self.game._board.update_board('x', '9')
        result = self.game.check_game_status()
        self.assertEqual(result, 'Tie')


class TestConsole(unittest.TestCase):
    """  A test suite for the Console class. """
    def setUp(self):
        """ Set up the test console. """
        self.console = Console()

    @patch('builtins.print')
    def test_print_string_returns_expected_output(self, mock_print):
        """ Test that print_string() prints the expected string to the console. """
        expected_output = "Welcome to Tic-Tac-Toe."
        self.console.print_string("Welcome to Tic-Tac-Toe.")
        mock_print.assert_called_with(expected_output)

    @patch('builtins.input', return_value='1')
    def test_prompt_input_returns_expected_output(self, mock_input):
        """ Test that prompt_input() returns the expected user input. """
        user_input = self.console.prompt_input("Enter a value: ")
        self.assertEqual(user_input, '1')


class TestBoard(unittest.TestCase):
    """ A test suite for the board class. """
    def setUp(self):
        """Set up a Board instance for testing"""
        self.test_board = Board()

    def test_get_board_returns_the_board_dictionary(self):
        """ Test that get_board() method returns the board dictionary. """
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.test_board.get_board()
        self.assertEqual(result, expected_result)

    def test_board_str(self):
        """ Test that the __str__() method returns the correct string representation of the board. """
        expected_output = "************************\n" \
                          "*    Current Board!    *\n" \
                          "************************\n" \
                          "*                      *\n" \
                          "*    1  |  2  |  3     *\n" \
                          "*  ------------------  *\n" \
                          "*    4  |  5  |  6     *\n" \
                          "*  ------------------  *\n" \
                          "*    7  |  8  |  9     *\n" \
                          "*                      *\n" \
                          "************************"
        self.assertEqual(str(self.test_board), expected_output)

    def test_update_board(self):
        """ Test that update_board() method correctly updates the board. """
        self.test_board.update_board("x", 1)
        expected_output = [["x", 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.test_board.get_board(), expected_output)

    def test_updating_the_board_twice(self):
        """ Test that updating the board twice with different values works as expected. """
        self.test_board.update_board("x", 1)
        self.test_board.update_board("o", 5)
        expected_output = [["x", 2, 3], [4, "o", 6], [7, 8, 9]]
        self.assertEqual(self.test_board.get_board(), expected_output)


class TestPlayer(unittest.TestCase):
    """ A test suite for the Player class. """
    def test_get_player_name_returns_players_name(self):
        """ Test if get_player_name returns the player's name. """
        expected_output = "1"
        result = Player("1", "x").get_player_name()
        self.assertEqual(result, expected_output)

    def test_get_player_mark_returns_players_mark(self):
        """ Test if get_player_mark returns the player's mark. """
        expected_output = "x"
        result = Player("1", "x").get_player_mark()
        self.assertEqual(result, expected_output)


class TestScore(unittest.TestCase):
    """ A test suite for the Score class."""

    def setUp(self):
        """ Set up the test score. """
        self.score = Score()

    def test_get_game_status_returns_false_if_game_is_not_won(self):
        """Test that get_game_status() returns False if the game is not won."""
        test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertFalse(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_row(self):
        """Test that get_game_status() returns True if the game is won in the first row."""
        test_board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_row(self):
        """Test that get_game_status() returns True if the game is won in the second row."""
        test_board = [[1, 2, 3], ['x', 'x', 'x'], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_column(self):
        """Test that get_game_status() returns True if the game is won in the first column."""
        test_board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_column(self):
        """Test that get_game_status() returns True if the game is won in the second column."""
        test_board = [[1, 'o', 3], [4, 'o', 6], [7, 'o', 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_descending(self):
        """Test that get_game_status() returns True if the game is won diagonally (descending)."""
        test_board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_ascending(self):
        """Test that get_game_status() returns True if the game is won diagonally (ascending)."""
        test_board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_tie(self):
        """Test that get_game_status() returns True if the game is a tie."""
        test_board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)


class TestTurn(unittest.TestCase):
    """A test suite for the Turn class."""

    def test_change_turn(self):
        """Test that change_turn() sets the current player turn."""
        expected_output = 2
        turn = Turn()
        turn.change_turn()
        result = turn.get_current_turn()
        self.assertEqual(result, expected_output)


class TestValidation(unittest.TestCase):
    """A test suite for the Validation class."""

    def setUp(self):
        """Set up the test board."""
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_validate_selection_valid(self):
        """Test that validate_selection() returns True for a valid selection."""
        result = Validation.validate_selection("1", self.test_board)
        self.assertTrue(result)

    def test_validate_selection_invalid(self):
        """Test that validate_selection() returns False for an invalid selection."""
        result = Validation.validate_selection("10", self.test_board)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
