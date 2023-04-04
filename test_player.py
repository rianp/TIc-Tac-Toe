import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """ A test suite for the Player class. """
    def test_get_player_name_returns_players_name(self):
        """ Test if get_player_name returns the player's name. """
        expected_output = "1"
        result = Player("1", "x").get_player_name()
        self.assertEqual(result, expected_output)

    def test_get_player_mark_returns_players_mark(self):
        """ Test if get_player_mark returns the player's mark. """
        expected_output = "x"
        result = Player("1", "x").get_player_mark()
        self.assertEqual(result, expected_output)
