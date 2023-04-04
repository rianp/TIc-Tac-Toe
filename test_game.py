import unittest
from game import Game


class TestGame(unittest.TestCase):
    """ A test suite for the Game class. """
    def setUp(self):
        """ Set up the test game. """
        self.game = Game()

    def test_validate_user_input_valid(self):
        """  Test that validate_user_input() returns the valid user input. """
        self.game._board.update_board('x', '1')
        result = self.game.validate_user_input('2')
        self.assertEqual(result, '2')

    def test_check_game_status_player1_wins_game(self):
        """ Test that check_game_status() returns True when player 1 wins. """
        self.game._board.update_board('x', '1')
        self.game._board.update_board('x', '2')
        self.game._board.update_board('x', '3')
        result = self.game.check_game_status()
        self.assertTrue(result)

    def test_check_game_status_player2_win(self):
        """ Test that check_game_status() returns True when player 2 wins. """
        self.game._board.update_board('o', '1')
        self.game._board.update_board('o', '4')
        self.game._board.update_board('o', '7')
        result = self.game.check_game_status()
        self.assertTrue(result)

    def test_check_game_status_tie(self):
        """ Test that check_game_status() returns 'Tie' when the game ends in a tie. """
        self.game._board.update_board('x', '1')
        self.game._board.update_board('o', '2')
        self.game._board.update_board('x', '3')
        self.game._board.update_board('x', '4')
        self.game._board.update_board('o', '5')
        self.game._board.update_board('o', '7')
        self.game._board.update_board('o', '6')
        self.game._board.update_board('x', '8')
        self.game._board.update_board('x', '9')
        result = self.game.check_game_status()
        self.assertEqual(result, 'Tie')
