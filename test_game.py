import unittest
from unittest.mock import MagicMock
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.players_mock = MagicMock()
        self.board_mock = MagicMock()
        self.console_mock = MagicMock()
        self.validator_mock = MagicMock()
        self.game = Game()

    def test_when_game_updates(self):
        player_mark = 'x'
        position = 1
        self.players_mock.get_current_player.return_value.get_mark.return_value = player_mark

        self.game.update_game(self.players_mock, position, self.board_mock)

        with self.subTest('should updated board'):
            self.board_mock.update_board.assert_called_once_with(player_mark, position)
        with self.subTest('should updated turn'):
            self.players_mock.change_turn.assert_called_once()

    def test_when_a_valid_move_is_made(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.console_mock.prompt_input.return_value = '4'

        move = self.game.get_move(board, self.console_mock, "Enter a value please: ", self.validator_mock)

        self.assertEqual(move, 4)
        self.console_mock.prompt_input.assert_called_once_with("Enter a value please: ")
        self.validator_mock.validate_move.assert_called_once_with('4', board, self.console_mock)

    def test_when_displaying_a_tied_game(self):
        board = [['o', 'x', 'o'], ['x', 'x', 'o'], ['x', 'o', 'x']]
        game_status = None
        result = self.game.display_game_status(game_status, self.players_mock, self.console_mock, board)
        with self.subTest('should return false'):
            self.assertFalse(result)
        with self.subTest('should return tie message'):
            self.console_mock.print_string.assert_called_with("Eek! Looks like it's a tie friends. Goodbye.")

    def test_when_displaying_a_won_game(self):
        board = [['o', 'o', 'o'], [4, 5, 6], [7, 8, 9]]
        self.players_mock.get_current_player.return_value.get_name.return_value = '1'
        game_status = True

        result = self.game.display_game_status(game_status, self.players_mock, self.console_mock, board)

        self.assertFalse(result)
        self.console_mock.print_string.assert_called_with("OMG! Congratulations Player 1, You won!")

    def test_when_displaying_an_unfinished_game(self):
        board = [['x', 2, 'o'], [4, 5, 6], [7, 8, 9]]
        game_status = False

        result = self.game.display_game_status(game_status, self.players_mock, self.console_mock, board)

        self.assertTrue(result)
        self.console_mock.print_string.assert_called_with(str(board))


