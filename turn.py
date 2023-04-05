class Turn:

    def __init__(self):
        self._turn = 1

    def change_turn(self):
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1

    def get_current_turn(self):
        return self._turn
