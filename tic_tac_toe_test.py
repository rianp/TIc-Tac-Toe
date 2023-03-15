""" This module contains a unit test suite for the application. """

import unittest
from unittest.mock import patch
from console import *
from board import *


class TestConsole(unittest.TestCase):
    """ A test suite for the Console class. """

    @patch('builtins.print')
    def test_print_string_returns_expected_output(self, mock_print_string):
        """ Test that print_string method of Console class returns the expected output. """

        expected_output = "Welcome to Tic-Tac-Toe."
        Console().print_string("Welcome to Tic-Tac-Toe.")
        mock_print_string.assert_called_with(expected_output)

class TestBoard(unittest.TestCase):
    """ A test suite for the Board class. """

    # def test_create_board_returns_the_expected_board_dictionary(self):
    #     """ Test that get_board method of Board class returns true. """
    #     expected_board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    #     self.assertEqual(Board().create_board(), expected_board)

    def test_get_board_returns_the_board_dictionary(self):
        """ Test that get_board method of Board class returns true. """
        expected_board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
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


if __name__ == '__main__':
    unittest.main()
