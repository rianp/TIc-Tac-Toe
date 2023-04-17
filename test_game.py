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

    def test_play_round(self):
        self.game.is_game_over = MagicMock(return_value=False)
        self.game.get_move = MagicMock(return_value=1)
        self.game.update_game = MagicMock()

        self.players.get_current_player.get_name.return_value = '1'

        self.game.play_round(self.board, self.players, self.console, self.validator)

        self.game.display_game_status.assert_called_with(False, self.players, self.console, self.board)


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
        string = "Enter a value please: "

        mock_validate_move = MagicMock(return_value=(True, None))
        self.validator.validate_move = mock_validate_move

        move = self.game.get_move(board, self.console, string, self.validator)

        with self.subTest('should prompt user for move'):
            self.console.prompt_input.assert_called_once_with("Enter a value please: ")
        with self.subTest('should validate the move'):
            mock_validate_move.assert_called_once_with('4', board)
        with self.subTest("should return the move if it's a valid choice"):
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


