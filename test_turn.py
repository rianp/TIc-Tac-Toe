import unittest
from turn import Turn


class TestTurn(unittest.TestCase):
    """A test suite for the Turn class."""

    def test_change_turn(self):
        """Test that change_turn() sets the current player turn."""
        expected_output = 2
        turn = Turn()
        turn.change_turn()
        result = turn.get_current_turn()
        self.assertEqual(result, expected_output)
