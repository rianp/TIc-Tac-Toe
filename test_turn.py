import unittest
from turn import Turn


class TestTurn(unittest.TestCase):

    def test_turn_updates_to_next_turn_when_turn_changes(self):
        expected_output = 2
        turn = Turn()
        turn.change_turn()
        result = turn.get_current_turn()
        self.assertEqual(result, expected_output)
