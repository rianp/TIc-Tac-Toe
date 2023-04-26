import unittest

from board import Board, WinnerStatus


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()

    def test_when_board_is_called(self):
        with self.subTest('should have cell numbers from 1 to 9'):
            expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            result = self.test_board.get_board()
            self.assertEqual(result, expected_result)

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
            self.assertEqual(result, WinnerStatus.ONGOING)

        with self.subTest('should check the state of the rows'):
            self.test_board._board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_X)

        with self.subTest('should check the state of the columns'):
            self.test_board._board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_X)

        with self.subTest('should check diagonal descending'):
            self.test_board._board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_O)

        with self.subTest('should check diagonal ascending'):
            self.test_board._board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_O)

        with self.subTest('round is finished when tied'):
            self.test_board._board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.DRAW)


class TestCustomBoard(unittest.TestCase):
    def test_build_board(self):
        with self.subTest('should build a 5x5 board when the selected board size is 5'):
            self.test_board = Board(5)

            result = self.test_board.get_size()
            self.assertEqual(result, 25)

        with self.subTest('should build a 7x7 board when the selected board size is 7'):
            self.test_board = Board(7)

            result = self.test_board.get_size()
            self.assertEqual(result, 49)

        with self.subTest('should build a board with the width matching the input number'):
            self.test_board = Board(5)
            expected_board = [[1, 2, 3, 4, 5],
                              [6, 7, 8, 9, 10],
                              [11, 12, 13, 14, 15],
                              [16, 17, 18, 19, 20],
                              [21, 22, 23, 24, 25]]

            result = self.test_board.get_board()
            self.assertEqual(result, expected_board)

    def test_when_updating_board(self):
        with self.subTest("should place player's mark on desired cell"):
            self.test_board = Board(5)
            self.test_board.update_board("x", 1)
            expected_output = [["x", 2, 3, 4, 5],
                               [6, 7, 8, 9, 10],
                               [11, 12, 13, 14, 15],
                               [16, 17, 18, 19, 20],
                               [21, 22, 23, 24, 25]]
            self.assertEqual(self.test_board.get_board(), expected_output)

    def test_get_board_state(self):
        self.test_board = Board(5)
        with self.subTest('game is not finished if there are no winners'):
            self.test_board._board = [[1, 2, 3, 4, 5],
                                      [6, 7, 8, 9, 10],
                                      [11, 12, 13, 14, 15],
                                      [16, 17, 18, 19, 20],
                                      [21, 22, 23, 24, 25]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.ONGOING)

        with self.subTest('should check the state of the rows'):
            self.test_board._board = [['x', 'x', 'x', 'x', 'x'],
                                      [6, 7, 8, 9, 10],
                                      [11, 12, 13, 14, 15],
                                      [16, 17, 18, 19, 20],
                                      [21, 22, 23, 24, 25]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_X)

        with self.subTest('should check the state of the columns'):
            self.test_board._board = [['x', 2, 3, 4, 5],
                                      ['x', 7, 8, 9, 10],
                                      ['x', 12, 13, 14, 15],
                                      ['x', 17, 18, 19, 20],
                                      ['x', 22, 23, 24, 25]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_X)

        with self.subTest('should check diagonal descending'):
            self.test_board._board = [['o', 2, 3, 4, 5],
                                      [6, 'o', 8, 9, 10],
                                      [11, 12, 'o', 14, 15],
                                      [16, 17, 18, 'o', 20],
                                      [21, 22, 23, 24, 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_O)

        with self.subTest('should check diagonal ascending'):
            self.test_board._board = [['o', 2, 3, 4, 'o'],
                                      [6, 7, 8, 'o', 10],
                                      [11, 12, 'o', 14, 15],
                                      [16, 'o', 18, 19, 20],
                                      ['o', 22, 23, 24, 25]]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.WINNER_O)

        with self.subTest('round is finished when tied'):
            self.test_board._board = [['x', 'o', 'x', 'o', 'x'],
                                      ['o', 'o', 'x', 'o', 'x'],
                                      ['o', 'x', 'o', 'x', 'o'],
                                      ['x', 'o', 'x', 'o', 'x'],
                                      ['o', 'x', 'o', 'x', 'o']]
            result = self.test_board.get_board_winner_status()
            self.assertEqual(result, WinnerStatus.DRAW)
