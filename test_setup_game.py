import unittest
from unittest.mock import Mock, MagicMock
from setup_game import SetUpGame


class TestSetUpGame(unittest.TestCase):
    def setUp(self):
        self.console = Mock()
        self.validator = Mock()
        self.players = MagicMock()
        self.computer_player = Mock()
        self.player = Mock()
        self.board = Mock()
        self.game = Mock()
        self.setup_game = SetUpGame(self.console, self.validator)

    def test_setup_game(self):
        self.setup_game.display_instructions = Mock()
        self.setup_game.create_players = Mock(return_value=self.players)
        self.setup_game.create_board = Mock(return_value=self.board)

        self.setup_game.setup_game()

        self.setup_game.display_instructions.assert_called_once()
        self.setup_game.create_players.assert_called_once()
        self.setup_game.create_board.assert_called_once()

    def test_display_instructions(self):
        self.setup_game.display_instructions()
        self.console.print_greeting.assert_called_once()
        self.console.print_instructions.assert_called_once()

    def test_create_players(self):
        self.setup_game.create_players()
        with self.subTest('should ask user for opponent choice when game starts'):
            self.console.selector.assert_called_with(
                "Let's pick your opponent!\nPress 1 for Human or press 2 for Computer: ",
                self.validator.validate_choice)

    def test_create_players_computer(self):
        self.console.selector.return_value = 2

        self.setup_game.create_players()
        self.players = MagicMock(self.computer_player, self.player)

        # self.players.assert_called_with(self.computer_player, self.player)
        self.computer_player.assert_called_once_with("1", "x")
        self.player.assert_called_once_with("2", "o")

    def test_create_board(self):
        self.validator.validate_size.return_value = 3
        self.console.selector.return_value = 3
        self.setup_game.create_board()

        with self.subTest('should create board with the size the user chooses'):
            self.console.selector.assert_called_with(
                "Let's build a board! Pick an odd number from 1 to 7: ", self.validator.validate_size)
