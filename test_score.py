import unittest
from score import Score


class TestScore(unittest.TestCase):
    """ A test suite for the Score class."""

    def setUp(self):
        """ Set up the test score. """
        self.score = Score

    def test_get_game_status_returns_false_if_game_is_not_won(self):
        """Test that get_game_status() returns False if the game is not won."""
        test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertFalse(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_row(self):
        """Test that get_game_status() returns True if the game is won in the first row."""
        test_board = [['x', 'x', 'x'], [4, 5, 6], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_row(self):
        """Test that get_game_status() returns True if the game is won in the second row."""
        test_board = [[1, 2, 3], ['x', 'x', 'x'], [7, 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_first_column(self):
        """Test that get_game_status() returns True if the game is won in the first column."""
        test_board = [['x', 2, 3], ['x', 5, 6], ['x', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_in_second_column(self):
        """Test that get_game_status() returns True if the game is won in the second column."""
        test_board = [[1, 'o', 3], [4, 'o', 6], [7, 'o', 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_descending(self):
        """Test that get_game_status() returns True if the game is won diagonally (descending)."""
        test_board = [['o', 2, 3], [4, 'o', 6], [7, 8, 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_won_diagonally_ascending(self):
        """Test that get_game_status() returns True if the game is won diagonally (ascending)."""
        test_board = [[1, 2, 'o'], [4, 'o', 6], ['o', 8, 9]]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)

    def test_get_game_status_returns_true_if_game_is_tie(self):
        """Test that get_game_status() returns True if the game is a tie."""
        test_board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['o', 'x', 'o']]
        result = self.score.get_game_status(test_board)
        self.assertTrue(result)
