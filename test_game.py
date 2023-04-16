import unittest
from unittest.mock import MagicMock
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.players = MagicMock()
        self.board = MagicMock()
        self.console = MagicMock()
        self.validator = MagicMock()
        self.game = Game()

    def test_when_game_updates(self):
        player_mark = 'x'
        position = 1
        self.players.get_current_player.return_value.get_mark.return_value = player_mark

        self.game.update_game(self.players, position, self.board)

        with self.subTest('should place players mark on board'):
            self.board.update_board.assert_called_once_with(player_mark, position)
        with self.subTest('should change player turn'):
            self.players.change_turn.assert_called_once()

    def test_when_getting_a_move(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.console.prompt_input.return_value = '4'

        move = self.game.get_move(board, self.console, "Enter a value please: ", self.validator)

        with self.subTest('should ask player for move'):
            self.console.prompt_input.assert_called_once_with("Enter a value please: ")
        with self.subTest("should check to see if the user's move is valid"):
            self.validator.validate_move.assert_called_once_with('4', board, self.console)
        with self.subTest("should return an integer"):
            self.assertEqual(move, 4)

    def test_when_displaying_a_tied_game(self):
        board = [['o', 'x', 'o'], ['x', 'x', 'o'], ['x', 'o', 'x']]
        game_status = None
        result = self.game.display_game_status(game_status, self.players, self.console, board)

        with self.subTest('should tell the players the game is tied'):
            self.console.print_string.assert_called_with("Eek! Looks like it's a tie friends. Goodbye.")
        with self.subTest('should exit game'):
            self.assertFalse(result)

    def test_when_displaying_a_won_game(self):
        board = [['o', 'o', 'o'], [4, 5, 6], [7, 8, 9]]
        self.players.get_current_player.return_value.get_name.return_value = '1'
        game_status = True

        result = self.game.display_game_status(game_status, self.players, self.console, board)

        with self.subTest('should congratulate the winner'):
            self.console.print_string.assert_called_with("OMG! Congratulations Player 1, You won!")
        with self.subTest('should exit game'):
            self.assertFalse(result)

    def test_when_displaying_an_unfinished_game(self):
        board = [['x', 2, 'o'], [4, 5, 6], [7, 8, 9]]
        game_status = False

        result = self.game.display_game_status(game_status, self.players, self.console, board)

        with self.subTest('should show the players the current state of the game'):
            self.console.print_string.assert_called_with(str(board))
        with self.subTest('should not exit game'):
            self.assertTrue(result)


