import unittest
from unittest.mock import MagicMock, Mock

from board import WinnerStatus
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        player_1 = ("1", "x")
        player_2 = ("2", "o")
        self.players = MagicMock(return_value=(player_1, player_2))
        self.board = MagicMock()
        self.console = MagicMock()
        self.validator = MagicMock()
        self.game = Game(self.board, self.players, self.console, self.validator)

    def test_play_round(self):
        current_player = self.players.get_current_player.return_value\
            = MagicMock(name='1', mark='x')
        self.game.get_move = MagicMock()

        with self.subTest("display current state of the game"):
            self.game.get_move = MagicMock()
            self.game.play_round()
            self.console.print_string.assert_called_once_with(str(self.board))

        with self.subTest("get current player's move to update the board"):
            self.game.get_move = MagicMock()
            self.game.play_round()
            self.game.get_move.assert_called()

        with self.subTest("update the board with the player's move "):
            self.game.update_game = MagicMock()
            self.game.play_round()
            self.game.update_game.assert_called()

        with self.subTest("return game over message when game is over"):
            current_player.get_name.return_value = '1'
            self.board.get_board_winner_status.return_value = WinnerStatus.WINNER_X
            expected_output = "OMG! Congratulations Player 1, You won!"
            result = self.game.play_round()
            self.assertEqual(result, expected_output)

        with self.subTest("return game over message when game is over"):
            current_player.get_name.return_value = '1'
            self.board.get_board_winner_status.return_value = True
            expected_output = "OMG! Congratulations Player 1, You won!"
            result = self.game.play_round()
            self.assertEqual(result, expected_output)

        with self.subTest("doesn't display a message if the game isn't over"):
            self.board.get_board_winner_status = \
                Mock(side_effect=[WinnerStatus.ONGOING, WinnerStatus.DRAW])
            self.game.get_message = Mock()
            self.game.play_round()
            self.assertEqual(self.game.get_message.call_count, 1)

        with self.subTest("play next round if game is not over"):
            self.board.get_board_winner_status = \
                Mock(side_effect=[WinnerStatus.ONGOING, WinnerStatus.ONGOING, WinnerStatus.DRAW])
            self.game.play_round()
            self.assertEqual(self.board.get_board_winner_status.call_count, 3)

    def test_when_game_updates(self):
        player_mark = 'x'
        move = 1

        self.game.update_game(player_mark, move)

        with self.subTest('should place players mark on board'):
            self.board.update_board.assert_called_once_with(player_mark, move)
        with self.subTest('should change player turn'):
            self.players.change_turn.assert_called_once()

    def test_when_getting_a_move(self):
        self.console.prompt_input.return_value = '4'
        mock_validate_move = MagicMock(return_value=4)
        self.game.validate_move = mock_validate_move

        move = self.game.get_move("Enter a value please: ")

        with self.subTest('should prompt user for move'):
            self.console.prompt_input.assert_called_once_with("Enter a value please: ")
        with self.subTest('should validate the move'):
            mock_validate_move.assert_called_once_with('4')
        with self.subTest("should return the move if it's a valid choice"):
            self.assertEqual(move, 4)

    def test_validate_move(self):
        with self.subTest(
                "should notify player their input isn't an integer if they entered a non-integer"
        ):
            user_input = "cookie"
            self.validator.is_valid_integer = Mock(return_value=False)

            result = self.game.validate_move(user_input)

            self.assertEqual(result, "Eek! That's not even a number! ")

        with self.subTest(
                "should notify player of out-of-bounds move if move is out of selectable range"
        ):
            user_input = "10"
            self.validator.is_valid_integer = Mock(return_value=True)
            self.validator.is_in_range = Mock(return_value=False)

            result = self.game.validate_move(user_input)

            self.assertEqual(result, "Whoa friend! This is outta bounds! ")

        with self.subTest(
                "should notify player of unavailable move when move has already been played"
        ):
            user_input = "4"
            self.validator.is_valid_integer = Mock(return_value=True)
            self.validator.is_in_range = Mock(return_value=True)
            self.validator.is_on_board = Mock(return_value=False)

            result = self.game.validate_move(user_input)

            self.assertEqual(result, "Rats! Someone already snagged this one! ")

    def test_get_message(self):
        player_mock = MagicMock()
        player_mock.get_name.return_value = '1'
        self.players.get_current_player.return_value = player_mock

        with self.subTest('should return tie message when the game is tied'):
            expected_output = "Eek! Looks like it's a tie friends. Goodbye."
            actual_output = self.game.get_message(WinnerStatus.DRAW)
            self.assertEqual(actual_output, expected_output)

        with self.subTest('should return winner message when the game is won'):
            expected_output = "OMG! Congratulations Player 1, You won!"
            player_mock.get_name.return_value = '1'
            actual_output = self.game.get_message(WinnerStatus.WINNER_X)
            self.assertEqual(actual_output, expected_output)

    def test_get_winner(self):
        player_mock = MagicMock()
        player_mock.get_name.return_value = '1'
        expected_output = '1'
        self.players.get_current_player.return_value = player_mock

        actual_output = self.game.get_winner()

        with self.subTest('should change player turn'):
            self.players.change_turn.assert_called_once()
        with self.subTest('should return winner'):
            self.assertEqual(actual_output, expected_output)
