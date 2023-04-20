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
        with self.subTest(
                "should notify player their input isn't an integer if they entered a non-integer"
        ):
            user_input = "cookie"
            self.validator.is_valid_integer = Mock(return_value=False)

            result = self.console.validate_move(user_input)

            self.assertEqual(result, "Eek! That's not even a number! ")

        with self.subTest(
                "should notify player of out-of-range size if board size is out of selectable range"
        ):
            user_input = "10"
            self.validator.is_valid_integer = Mock(return_value=True)
            self.validator.is_in_range = Mock(return_value=False)

            result = self.console.validate_move(user_input)

            self.assertEqual(result, "Whoa friend! This is outta bounds! ")
            
        with self.subTest(
                "should notify player of even size if chosen size isn't odd"
        ):
            user_input = "4"
            self.validator.is_valid_integer = Mock(return_value=True)
            self.validator.is_in_range = Mock(return_value=True)

            result = self.console.validate_move(user_input)

            self.assertEqual(result, "Whoa friend! This is outta bounds! ")
