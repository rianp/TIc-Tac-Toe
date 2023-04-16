import unittest
from unittest.mock import Mock
from validation import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.validator = Validator()

    def test_is_on_board(self):
        test_board = [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
        with self.subTest('returns true when selection is available'):
            result = self.validator.is_on_board(1, test_board)
            self.assertTrue(result)

        with self.subTest('returns false when selection is not available'):
            result = self.validator.is_on_board(4, test_board)
            self.assertFalse(result)

    def test_is_in_range(self):
        board_range = range(1, len(self.test_board) * len(self.test_board) + 1)
        with self.subTest('returns true when selection is at minimum selection range'):
            result = self.validator.is_in_range(1, board_range)
            self.assertTrue(result)

        with self.subTest('returns true when selection is at maximum selection range'):
            result = self.validator.is_in_range(9, board_range)
            self.assertTrue(result)

        with self.subTest('returns false when selection is lower than selection range'):
            result = self.validator.is_in_range(0, board_range)
            self.assertFalse(result)

        with self.subTest('returns false when selection is higher than selection range'):
            result = self.validator.is_in_range(10, board_range)
            self.assertFalse(result)

    def test_is_valid_integer(self):
        with self.subTest('returns false when input is a character'):
            result = self.validator.is_valid_integer("r")
            self.assertFalse(result)

        with self.subTest('returns false when input is none'):
            result = self.validator.is_valid_integer("")
            self.assertFalse(result)

        with self.subTest('returns false when input is a space'):
            result = self.validator.is_valid_integer(" ")
            self.assertFalse(result)

        with self.subTest('returns false when input has leading whitespace'):
            result = self.validator.is_there_whitespace(" 1")
            self.assertFalse(result)

        with self.subTest('returns false when input has trailing whitespace'):
            result = self.validator.is_there_whitespace("1 ")
            self.assertFalse(result)

    def test_when_players_move_is_not_an_integer(self):
        user_input = "hello"
        board = Mock()
        console = Mock()
        with self.subTest("should tell the players it's not an integer"):
            self.assertFalse(self.validator.validate_move(user_input, board, console))
            console.print_string.assert_called_once_with("Eek! That's not even a number! ")

    def test_when_players_move_is_out_of_bounds(self):
        user_input = "10"
        board = Mock()
        board.get_board_range.return_value = range(1, 10)
        console = Mock()
        with self.subTest("should tell the player their move is out of bounds"):
            self.assertFalse(self.validator.validate_move(user_input, board, console))
            console.print_string.assert_called_once_with("Whoa friend! This is outta bounds! ")

    def test_when_players_move_is_already_taken(self):
        user_input = "4"
        board = Mock()
        board.get_board_range.return_value = range(1, 10)
        board.get_board.return_value = [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
        console = Mock()
        with self.subTest("should tell the player their move has already been played"):
            self.assertFalse(self.validator.validate_move(user_input, board, console))
            console.print_string.assert_called_once_with("Rats! Someone already snagged this one! ")
