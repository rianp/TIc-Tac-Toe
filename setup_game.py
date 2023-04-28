from game import Game
from board import Board
from player import Player, ComputerPlayer
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
        choice = self.console.selector(
            "Let's pick your opponent!"
            "\nPress 1 for Human or press 2 for Computer: ", self.validator.validate_choice)
        if choice == 1:
            return Players(Player("1", "x"), Player("2", "o"))
        else:
            return Players(ComputerPlayer("1", "x"), Player("2", "o"))

    def create_board(self):
        board_size = self.console.selector(
            "Let's build a board! Pick an odd number from 1 to 7: ", self.validator.validate_size)
        return Board(board_size)
