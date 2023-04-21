import unittest
from io import StringIO
from unittest.mock import Mock, patch
from console import Console


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = Console()
        self.validator = Mock()

    def test_print_string(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.print_string("This is Tic-Tac-Toooeee!!!!")
            self.assertEqual(fake_out.getvalue().strip(), "This is Tic-Tac-Toooeee!!!!")

    def test_prompt_input(self):
        with patch('builtins.input', return_value='pizza'):
            result = self.console.prompt_input("Enter a string: ")
            self.assertEqual(result, "pizza")

    def test_print_greeting(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.print_greeting()
            self.assertIn("(Ⓘ‿‿Ⓘ)", fake_output.getvalue())
            self.assertIn("Welcome to Tic-Tac-Toe!!!", fake_output.getvalue())

    def test_print_instructions(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.print_instructions()
            self.assertIn("Here are the instructions to the game!", fake_output.getvalue())
            self.assertIn("all fields are taken", fake_output.getvalue())

    def test_select_board_size(self):
        prompt = "enter a number: "
        self.console.prompt_input = Mock(return_value='3')
        validated_size_mock = Mock()
        validated_size_mock.is_valid = True
        validated_size_mock.message = "wrong num"
        self.validator.validate_size = Mock(return_value=validated_size_mock)

        size = self.console.select_board_size(prompt, self.validator)

        with self.subTest('should prompt user for board size'):
            self.console.prompt_input.assert_called_once_with(prompt)
        with self.subTest('should validate the size'):
            self.validator.validate_size.assert_called_once_with('3')
        with self.subTest("should return the size if it's a valid choice"):
            self.assertEqual(size, 3)
