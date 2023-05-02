from game import Game
from board import Board
from player import Player, ComputerPlayer, SuperComputerPlayer
from players import Players


class SetUpGame:
    def __init__(self, console, validator):
        self.console = console
        self.validator = validator

    def setup_game(self):
        self.display_instructions()
        players = self.create_players()
        board = self.create_board()

        game = Game(board, players, self.console, self.validator)

        return game

    def display_instructions(self):
        self.console.print_greeting()
        self.console.print_instructions()

    def create_players(self):
        choice = self.console.get_integer_input(
            "Let's pick your opponent!"
            "\nPress 1 for Human, "
            "press 2 for Easy Peasy Computer, "
            "or press 3 for Extremely Difficult Computer: ", self.validator.validate_menu_choice)

        if choice == 1:
            return Players(Player("1", "x"), Player("2", "o"))

        if choice == 2:
            return Players(ComputerPlayer("Bot", "x"), Player("2", "o"))

        return Players(SuperComputerPlayer("Super Bot", "x"), Player("2", "o"))

    def create_board(self):
        board_size = self.console.get_integer_input(
            "Let's build a board! Enter a board size of either 3 or 5: ", self.validator.validate_size)
        return Board(board_size)
