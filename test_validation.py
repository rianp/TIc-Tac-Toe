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
