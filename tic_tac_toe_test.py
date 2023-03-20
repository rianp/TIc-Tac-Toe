""" This module contains a unit test suite for the application. """

import unittest
from unittest.mock import patch
from console import *
from board import *
from players import *

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
        self.assertEqual(Board().get_board(), expected_board)

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
        test_board = Board()
        test_board.update_board("x", 1)
        test_board.update_board("o", 5)
        expected_output = [["x", 2, 3], [4, "o", 6], [7, 8, 9]]
        self.assertEqual(test_board.get_board(), expected_output)

class TestPlayers(unittest.TestCase):
    """ A test suite for the PLayer class. """

    def test_get_player_1_returns_x(self):
        """ Test that get player 1 will return x. """
        expected_player = "x"
        self.assertEqual(Players().get_player(1), expected_player)

    def test_get_player_2_returns_o(self):
        """ Test that get player 2 will return o. """
        expected_player = "o"
        self.assertEqual(Players().get_player(2), expected_player)


if __name__ == '__main__':
    unittest.main()
