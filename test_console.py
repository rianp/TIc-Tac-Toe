import unittest
from io import StringIO
from unittest.mock import Mock, patch
from console import Console, Formatter


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


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.formatter = Formatter(self.board)

    def test_build_board_layout(self):
        with self.subTest("should make the board pretty if the width of the board is 3."):
            self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            self.formatter = Formatter(self.board)
            size = len(self.board)
            expected_board_layout = (
                "*    1  |  2  |  3    *\n"
                "*    -------------    *\n"
                "*    4  |  5  |  6    *\n"
                "*    -------------    *\n"
                "*    7  |  8  |  9    *\n"
            )
            result = self.formatter.build_board_layout(size)
            self.assertEqual(result, expected_board_layout)

        with self.subTest("should make the board pretty if the width of the board is 5."):
            self.board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
            self.formatter = Formatter(self.board)
            size = len(self.board)
            expected_board_layout = (
                "*     1  |   2  |   3  |   4  |   5    *\n"
                "*    ------------------------------    *\n"
                "*     6  |   7  |   8  |   9  |  10    *\n"
                "*    ------------------------------    *\n"
                "*    11  |  12  |  13  |  14  |  15    *\n"
                "*    ------------------------------    *\n"
                "*    16  |  17  |  18  |  19  |  20    *\n"
                "*    ------------------------------    *\n"
                "*    21  |  22  |  23  |  24  |  25    *\n"
            )
            result = self.formatter.build_board_layout(size)
            self.assertEqual(result, expected_board_layout)

    def test_build_header(self):
        with self.subTest("should make a centered header with the width matching the given size"):
            width = 23
            expected_header = (
                "***********************\n"
                "*   Current Board!   *\n"
                "***********************\n"
            )
            result = self.formatter.build_header(width)
            self.assertEqual(result, expected_header)

    def test_build_footer(self):
        with self.subTest("should make a footer row with the width matching the size given."):
            expected_footer = "***********************\n"
            result = self.formatter.build_footer(23)
            self.assertEqual(result, expected_footer)

    def test_calc_board_width(self):
        with self.subTest("should calculate the width of the board."):
            board = "*    1  |  2  |  3    *\n"
            "*    -------------    *\n"
            "*    4  |  5  |  6    *\n"
            "*    -------------    *\n"
            "*    7  |  8  |  9    *\n"
            expected_width = 23
            result = self.formatter.calc_board_width(board)
            self.assertEqual(result, expected_width)

    def test_build_layout(self):
        with self.subTest("should make a pretty board layout."):
            expected_layout = (
                "***********************\n"
                "*   Current Board!   *\n"
                "***********************\n"
                "*    1  |  2  |  3    *\n"
                "*    -------------    *\n"
                "*    4  |  5  |  6    *\n"
                "*    -------------    *\n"
                "*    7  |  8  |  9    *\n"
                "***********************\n"
            )
            result = self.formatter.build_layout()
            self.assertEqual(result, expected_layout)

        with self.subTest("should make a pretty board layout."):
            self.board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                            [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
            self.formatter = Formatter(self.board)

            expected_layout = (
                "****************************************\n"
                "*            Current Board!            *\n"
                "****************************************\n"
                "*     1  |   2  |   3  |   4  |   5    *\n"
                "*    ------------------------------    *\n"
                "*     6  |   7  |   8  |   9  |  10    *\n"
                "*    ------------------------------    *\n"
                "*    11  |  12  |  13  |  14  |  15    *\n"
                "*    ------------------------------    *\n"
                "*    16  |  17  |  18  |  19  |  20    *\n"
                "*    ------------------------------    *\n"
                "*    21  |  22  |  23  |  24  |  25    *\n"
                "****************************************\n"
            )
            result = self.formatter.build_layout()
            self.assertEqual(result, expected_layout)
