import unittest
from validation import *


class TestValidation(unittest.TestCase):
    """A test suite for the Validation class."""

    def setUp(self):
        """Set up the test board."""
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_validate_selection_valid(self):
        """Test that validate_selection() returns True for a valid selection."""
        result = Validation.validate_selection("1", self.test_board)
        self.assertTrue(result)

    def test_validate_selection_invalid(self):
        """Test that validate_selection() returns False for an invalid selection."""
        result = Validation.validate_selection("10", self.test_board)
        self.assertFalse(result)