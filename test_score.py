""" Maybe throw score into game file. """
import unittest
from score import Score


class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score

    def test_get_game_status(self):
        with self.subTest('round is unfinished when no winners or tie'):
            test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            result = self.score.get_game_status(test_board)
            self.assertFalse(result)

        with self.subTest('round is finished when won in row'):
            test_board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
            result = self.score.get_game_status(test_board)
            self.assertTrue(result)

        with self.subTest('round is finished when won in column'):
            test_board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
            result = self.score.get_game_status(test_board)
            self.assertTrue(result)

        with self.subTest('round is finished when won diagonally descending'):
            test_board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
            result = self.score.get_game_status(test_board)
            self.assertTrue(result)

        with self.subTest('round is finished when won diagonally ascending'):
            test_board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
            result = self.score.get_game_status(test_board)
            self.assertTrue(result)

        with self.subTest('round is finished when tied'):
            test_board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
            result = self.score.get_game_status(test_board)
            self.assertTrue(result)
