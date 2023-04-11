import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()

    def test_has_board(self):
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.test_board.get_board()
        self.assertEqual(result, expected_result)

    def test_displays_board(self):
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

    def test_updates_board(self):
        self.test_board.update_board("x", 1)
        expected_output = [["x", 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.test_board.get_board(), expected_output)
