"""
This module defines a `Turn` class representing the turns for the Tic-Tac-Toe game.
"""


class Turn:
    """ A class representing a turn for a Tic-Tac-Toe game. """

    def __init__(self):
        self._turn = ("", "")

    def change_turn(self, players):
        """ Changes player turn. """
        players = players.get_players()
        if self._turn[0] == players[0]:
            self._turn = (players[1], "o")
        else:
            self._turn = (players[0], "x")
        return

    def get_current_turn(self):
        """ Returns the current player turn. """
        return self._turn


