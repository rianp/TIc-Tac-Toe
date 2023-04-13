import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_validate_user_input(self):
        with self.subTest('returns true when input is valid'):
            game = Game()
            result = game.validate_user_input(2)
            self.assertTrue(result)

    def test_check_game_status(self):
        with self.subTest('round is won when player 1 wins'):
            game = Game()
            game._board.update_board('x', 1)
            game._board.update_board('x', 2)
            game._board.update_board('x', 3)
            result = game.check_game_status()
            self.assertTrue(result)

        with self.subTest('round is won when player 2 wins'):
            game = Game()
            game._board.update_board('o', 1)
            game._board.update_board('o', 4)
            game._board.update_board('o', 7)
            result = game.check_game_status()
            self.assertTrue(result)

        with self.subTest('round ties when no one wins'):
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


