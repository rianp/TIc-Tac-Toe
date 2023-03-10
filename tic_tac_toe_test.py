""" This module contains a unit test suite for the application. """

import unittest
from unittest.mock import patch
from console import *


class TestConsole(unittest.TestCase):
    """ A test suite for the Console class. """

    @patch('builtins.print')
    def test_print_string_returns_true(self, mock_print_string):
        """ Test that print_string method of Console class returns the expected output. """

        expected_output = "Welcome to Tic-Tac-Toe."
        Console().print_string("Welcome to Tic-Tac-Toe.")
        mock_print_string.assert_called_with(expected_output)


if __name__ == '__main__':
    unittest.main()
