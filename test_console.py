import unittest
from io import StringIO
from unittest.mock import patch
from console import Console


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = Console()

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
