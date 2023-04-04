import unittest
from board import *


class TestBoard(unittest.TestCase):
    """ A test suite for the board class. """
    def setUp(self):
        """Set up a Board instance for testing"""
        self.test_board = Board()

    def test_get_board_returns_the_board_dictionary(self):
        """ Test that get_board() method returns the board dictionary. """
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.test_board.get_board()
        self.assertEqual(result, expected_result)

    def test_board_str(self):
        """ Test that the __str__() method returns the correct string representation of the board. """
        expected_output = "************************\n" \
                          "*    Current Board!    *\n" \
                          "************************\n" \
                          "*                      *\n" \
                          "*    1  |  2  |  3     *\n" \
                          "*  ------------------  *\n" \
                          "*    4  |  5  |  6     *\n" \
                          "*  ------------------  *\n" \
                          "*    7  |  8  |  9     *\n" \
                          "*                      *\n" \
                          "************************"
        self.assertEqual(str(self.test_board), expected_output)

    def test_update_board(self):
        """ Test that update_board() method correctly updates the board. """
        self.test_board.update_board("x", 1)
        expected_output = [["x", 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.test_board.get_board(), expected_output)

    def test_updating_the_board_twice(self):
        """ Test that updating the board twice with different values works as expected. """
        self.test_board.update_board("x", 1)
        self.test_board.update_board("o", 5)
        expected_output = [["x", 2, 3], [4, "o", 6], [7, 8, 9]]
        self.assertEqual(self.test_board.get_board(), expected_output)