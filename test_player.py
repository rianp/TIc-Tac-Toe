import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def test_has_name_when_name_is_given(self):
        player = Player("1", "x")
        expected_output = "1"
        result = player.get_name()
        self.assertEqual(result, expected_output)

    def test_has_mark_when_mark_is_given(self):
        player = Player("2", "o")
        expected_output = "o"
        result = player.get_mark()
        self.assertEqual(result, expected_output)

    # need to write tests checking for no name or mark given
