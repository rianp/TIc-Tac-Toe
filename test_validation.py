import unittest
from validation import Validator


class TestUserInputValidation(unittest.TestCase):

    def setUp(self):
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.validator = Validator

    def test_returns_true_when_in_range_integers(self):
        result = self.validator.validate_selection(1, self.test_board)
        self.assertTrue(result)

    def test_returns_false_when_out_of_range_integers(self):
        result = self.validator.validate_selection(10, self.test_board)
        self.assertFalse(result)

    def test_returns_false_when_non_integers(self):
        result = self.validator.validate_selection("r", self.test_board)
        self.assertFalse(result)
