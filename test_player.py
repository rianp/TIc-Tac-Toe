import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def test_player(self):
        with self.subTest('has name'):
            player = Player("1", "x")
            expected_output = "1"
            result = player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            player = Player("2", "o")
            expected_output = "o"
            result = player.get_mark()
            self.assertEqual(result, expected_output)

    # need to write tests checking for no name or mark given
