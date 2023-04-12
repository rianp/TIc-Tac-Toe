import unittest
from turn import Turn


class TestTurn(unittest.TestCase):

    def test_turn_changes_when_change_turn(self):
        expected_output = 2
        turn = Turn()
        turn.change_turn()
        result = turn.get_current_turn()
        self.assertEqual(result, expected_output)
