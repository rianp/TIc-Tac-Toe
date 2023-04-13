import unittest
from validation import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.validator = Validator

    def test_validate_selection(self):
        with self.subTest('returns true when in range integers'):
            result = self.validator.validate_selection(1, self.test_board)
            self.assertTrue(result)

        with self.subTest('returns false when out of range integers'):
            result = self.validator.validate_selection(10, self.test_board)
            self.assertFalse(result)

        with self.subTest('returns false when non integers'):
            result = self.validator.validate_selection("r", self.test_board)
            self.assertFalse(result)
