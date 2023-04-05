import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("1", "x")

    def test_has_name(self):
        expected_output = "1"
        result = self.player.get_name()
        self.assertEqual(result, expected_output)

    def test_has_mark(self):
        expected_output = "x"
        result = self.player.get_mark()
        self.assertEqual(result, expected_output)
