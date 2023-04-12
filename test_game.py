import unittest
from game import Game


class TestGameValidation(unittest.TestCase):
    def test_returns_true_when_input_is_valid(self):
        game = Game()
        result = game.validate_user_input(2)
        self.assertTrue(result)

class TestCheckGameStatus(unittest.TestCase):
    def test_game_won_when_player_1_wins(self):
        game = Game()
        game._board.update_board('x', 1)
        game._board.update_board('x', 2)
        game._board.update_board('x', 3)
        result = game.check_game_status()
        self.assertTrue(result)

    def test_game_won_when_player_2_wins(self):
        game = Game()
        game._board.update_board('o', 1)
        game._board.update_board('o', 4)
        game._board.update_board('o', 7)
        result = game.check_game_status()
        self.assertTrue(result)

    def test_game_ties_when_no_winners(self):
        game = Game()
        game._board.update_board('x', 1)
        game._board.update_board('o', 2)
        game._board.update_board('x', 3)
        game._board.update_board('x', 4)
        game._board.update_board('o', 5)
        game._board.update_board('o', 7)
        game._board.update_board('o', 6)
        game._board.update_board('x', 8)
        game._board.update_board('x', 9)
        result = game.check_game_status()
        self.assertEqual(result, 'Tie')

