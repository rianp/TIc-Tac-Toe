import unittest
from unittest.mock import Mock, patch
from setup_game import SetUpGame, Player, Players, ComputerPlayer, SuperComputerPlayer
from board import Board


class TestSetUpGame(unittest.TestCase):
    def setUp(self):
        self.console = Mock()
        self.validator = Mock()
        self.player = Mock()
        self.players = Mock()
        self.board = Mock()
        self.setup_game = SetUpGame(self.console, self.validator)

    @patch('setup_game.Game')
    def test_setup_game(self, game):
        self.player.get_name.return_value = 'Player 1'
        self.players.get_players.return_value = [self.player]
        self.setup_game.display_instructions = Mock()
        self.setup_game.create_players = Mock(return_value=self.players)
        self.setup_game.create_board = Mock(return_value=self.board)
        game.return_value = game

        self.setup_game.setup_game()
        with self.subTest('should show the instructions to the users when game starts'):
            self.setup_game.display_instructions.assert_called_once()
        with self.subTest('should create players when the game is setting up'):
            self.setup_game.create_players.assert_called_once()
        with self.subTest('should create a board when the game is setting up'):
            self.setup_game.create_board.assert_called_once_with('Player 1')
        with self.subTest('should set up the game with the created board and players'):
            game.assert_called_once_with(self.board, self.players, self.console, self.validator)

    def test_display_instructions(self):
        self.setup_game.display_instructions()
        self.console.print_greeting.assert_called_once()
        self.console.print_instructions.assert_called_once()

    def test_create_players(self):
        self.setup_game.create_players()

        with self.subTest('should ask user for opponent choice when game starts'):
            self.console.get_integer_input.assert_called_with(
                "Let's pick your opponent!"
                "\nPress 1 for Human, "
                "press 2 for Easy Peasy Computer, "
                "or press 3 for Extremely Difficult Computer: ",
                self.validator.validate_menu_choice)

        with self.subTest(
                'should set the players to human vs human if human is selected as opponent'):
            self.console.get_integer_input.return_value = 1
            players = self.setup_game.create_players()
            expected_players = Players(ComputerPlayer("1", "x"), Player("2", "o"))
            self.assertEqual(
                players.get_players()[0].get_name(), expected_players.get_players()[0].get_name())

        with self.subTest(
                'should set the players to computer vs human if computer is selected as opponent'):
            self.console.get_integer_input.return_value = 2
            players = self.setup_game.create_players()
            expected_players = Players(ComputerPlayer("Bot", "x"), Player("2", "o"))
            self.assertEqual(
                players.get_players()[0].get_name(), expected_players.get_players()[0].get_name())

        with self.subTest(
                'should set the players to computer vs human if computer is selected as opponent'):
            self.console.get_integer_input.return_value = 3
            players = self.setup_game.create_players()
            expected_players = Players(SuperComputerPlayer("Super Bot", "x"), Player("2", "o"))
            self.assertEqual(
                players.get_players()[0].get_name(), expected_players.get_players()[0].get_name())

    def test_create_board(self):
        self.validator.validate_size.return_value = 3
        self.console.get_integer_input.return_value = 3

        with self.subTest('should create board with the size the user chooses when opponent is human'):
            self.setup_game.create_board("1")
            self.console.get_integer_input.assert_called_with(
                "Let's build a board! Enter a board size of either 3 or 5: ",
                self.validator.validate_size)

        with self.subTest('should create board with the size the user chooses when opponent is Bot'):
            self.setup_game.create_board("Bot")
            self.console.get_integer_input.assert_called_with(
                "Let's build a board! Enter a board size of either 3 or 5: ",
                self.validator.validate_size)

        with self.subTest('should automatically create a 3x3 board when opponent is Super Bot'):
            board = self.setup_game.create_board("Super Bot")
            self.assertIsInstance(board, Board)
            self.assertEqual(len(board.get_board()), 3)
