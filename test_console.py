import unittest
from unittest.mock import patch
from console import *


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
        result = self.console.prompt_input("Enter a value: ")
        self.assertEqual(result, '1')