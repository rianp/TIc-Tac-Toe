import unittest
from turn import Turn


class TestTurn(unittest.TestCase):

    def test_change(self):
        with self.subTest('turn changes'):
            expected_output = 2
            turn = Turn()
            turn.change_turn()
            result = turn.get_current_turn()
            self.assertEqual(result, expected_output)
