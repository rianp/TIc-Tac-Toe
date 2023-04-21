import unittest
from players import Players


class TestPlayers(unittest.TestCase):

    def test_init(self):
        players = Players("Player 1", "Player 2")
        self.assertEqual(players.get_players(), ("Player 1", "Player 2"))

    def test_change_turn(self):
        with self.subTest('should change to the specified players turn'):
            players = Players("Player 1", "Player 2")
            players.change_turn()
            self.assertEqual(players.get_current_player(), "Player 2")
            players.change_turn()
            self.assertEqual(players.get_current_player(), "Player 1")

    def test_get_current_player(self):
        with self.subTest('should return the player who is currently taking their turn'):
            players = Players("Player 1", "Player 2")
            self.assertEqual(players.get_current_player(), "Player 1")
            players.change_turn()
            self.assertEqual(players.get_current_player(), "Player 2")
