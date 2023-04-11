""" Maybe throw score into game file. """
import unittest
from score import Score


class TestCheckGameStatus(unittest.TestCase):
    def setUp(self):
        self.score = Score

    def test_not_won(self):
        test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertFalse(result)

    def test_won_in_row(self):
        test_board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_won_in_column(self):
        test_board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_won_diagonally_descending(self):
        test_board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_won_diagonally_ascending(self):
        test_board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_tied(self):
        test_board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)
