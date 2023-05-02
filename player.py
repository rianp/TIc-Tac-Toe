class Player:
    def __init__(self, name, mark):
        self._name = name
        self._mark = mark

    def get_name(self):
        return self._name

    def get_mark(self):
        return self._mark


class ComputerPlayer:
    def __init__(self, name, mark):
        self.player = Player(name, mark)

    def get_name(self):
        return self.player.get_name()

    def get_mark(self):
        return self.player.get_mark()

    def make_move(self, board):
        for row in board:
            for cell in row:
                if isinstance(cell, int):
                    return cell
        return 0


class SuperComputerPlayer:
    def __init__(self, name, mark):
        self.player = Player(name, mark)

    def get_name(self):
        return self.player.get_name()

    def get_mark(self):
        return self.player.get_mark()
