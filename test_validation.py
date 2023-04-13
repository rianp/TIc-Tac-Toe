import unittest
from validation import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.validator = Validator

    def test_is_on_board(self):
        test_board = [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
        with self.subTest('returns true when selection is still on board'):
            result = self.validator.is_on_board(1, test_board)
            self.assertTrue(result)

        with self.subTest('returns false when selection is not on board'):
            result = self.validator.is_on_board(4, test_board)
            self.assertFalse(result)

    def test_is_in_range(self):
        with self.subTest('returns true when selection is in selection range'):
            result = self.validator.is_in_range(1, self.test_board)
            self.assertTrue(result)

        with self.subTest('returns true when selection is in selection range'):
            result = self.validator.is_in_range(9, self.test_board)
            self.assertTrue(result)

        with self.subTest('returns false when selection is out of selection range'):
            result = self.validator.is_in_range(10, self.test_board)
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
