""" This module contains a unit test suite for the application. """

import unittest
from unittest.mock import patch
from console import *
from board import *
from players import *
from score import *
from turn import *

class TestConsole(unittest.TestCase):
    """ A test suite for the Console class. """

    @patch('builtins.print')
    def test_print_string_returns_expected_output(self, mock_print):
        """ Test that print_string method of Console class returns the expected output. """

        expected_output = "Welcome to Tic-Tac-Toe."
        Console.print_string("Welcome to Tic-Tac-Toe.")
        mock_print.assert_called_with(expected_output)

    @patch('builtins.input', return_value='1')
    def test_prompt_input_returns_expected_output(self, mock_input):
        """ Test that input_string method of Console class returns the expected output. """
        user_input = Console.prompt_input("Enter a value: ")
        self.assertEqual(user_input, '1')

class TestBoard(unittest.TestCase):
    """ A test suite for the Board class. """

    def test_get_board_returns_the_board_dictionary(self):
        """ Test that get_board method of Board class returns true. """
        expected_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = Board().get_board()
        self.assertEqual(result, expected_board)

    def test_board_str(self):
        """Test that the board string method returns a formatted board as a string."""
        test_board = Board()
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

        self.assertEqual(str(test_board), expected_output)

    def test_update_board(self):
        """ Test that the update board method returns the correct output. """
        test_board = Board()
        test_board.update_board("x", 1)
        expected_output = [["x", 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(test_board.get_board(), expected_output)

    def test_updating_the_board_twice(self):
        """ Test that the update board method returns the correct output after updating the board twice. """
        expected_output = [["x", 2, 3], [4, "o", 6], [7, 8, 9]]
        test_board = Board()
        test_board.update_board("x", 1)
        test_board.update_board("o", 5)
        result = test_board.get_board()
        self.assertEqual(result, expected_output)

class TestPlayers(unittest.TestCase):
    """ A test suite for the Player class. """

    def test_get_players_returns_players_tuple(self):
        """ Test that get player 1 will return x. """
        expected_output = ("Player 1", "Player 2")
        result = Players().get_players()
        self.assertEqual(result, expected_output)


class TestScore(unittest.TestCase):
    """ A test suit for the Score class. """

    def test_get_game_status_returns_false_if_game_is_not_won(self):
        """ Test that game status will return false. """
        test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = Score().get_game_status(test_board)
        self.assertFalse(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_row(self):
        """ Test that game status will return true. """
        test_board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_row(self):
        """ Test that game status will return true. """
        test_board = [[1, 2, 3], ['x', 'x', 'x'], [7, 8, 9]]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_column(self):
        """ Test that game status will return true. """
        test_board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_column(self):
        """ Test that game status will return true. """
        test_board = [[1, 'o', 3], [4, 'o', 6], [7, 'o', 9]]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_descending(self):
        """ Test that game status will return true. """
        test_board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_ascending(self):
        """ Test that game status will return true. """
        test_board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_tie(self):
        """ Test that game status will return true. """
        test_board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
        result = Score().get_game_status(test_board)
        self.assertTrue(result)


class TestTurn(unittest.TestCase):
    """ A test suite for the Turn class. """

    def test_change_turn_sets_the_current_player_turn(self):
        test_players = Players()
        expected_output = ("Player 1", "x")
        test_turn = Turn()
        test_turn.change_turn(test_players)
        result = test_turn.get_current_turn()
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
