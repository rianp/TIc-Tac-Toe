import unittest

from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()

    def test_when_board_is_called(self):
        with self.subTest('should have cell numbers from 1 to 9'):
            expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            result = self.test_board.get_board()
            self.assertEqual(result, expected_result)

        with self.subTest('should be pretty when displayed'):
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

    def test_when_getting_board_range(self):
        with self.subTest('should return range from lowest to highest cell number'):
            board_length = len(self.test_board.get_board())
            board_range = range(1, board_length * board_length)
            expected_output = range(1, 9)
            self.assertEqual(board_range, expected_output)

    def test_when_updating_board(self):
        with self.subTest("should place player's mark on desired cell"):
            self.test_board.update_board("x", 1)
            expected_output = [["x", 2, 3], [4, 5, 6], [7, 8, 9]]
            self.assertEqual(self.test_board.get_board(), expected_output)

    def test_get_board_state(self):
        with self.subTest('game is not finished if there are no winners'):
            self.test_board._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertFalse(result)

        with self.subTest('should check the state of the rows'):
            self.test_board._board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertTrue(result)

        with self.subTest('should check the state of the columns'):
            self.test_board._board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertTrue(result)

        with self.subTest('should check diagonal descending'):
            self.test_board._board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertTrue(result)

            with self.subTest('should check diagonal ascending'):
                self.test_board._board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
                result = self.test_board.get_board_winner_status()
                self.assertTrue(result)

        with self.subTest('round is finished when tied'):
            self.test_board._board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertIsNone(result)
