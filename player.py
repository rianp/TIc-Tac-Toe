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

    def make_move(self, board):
        best_weight = -1000
        best_position = (-1, -1)

        if self.is_no_moves_made(board):
            return board[len(board) % 2][len(board) % 2]

        for row in range(len(board)):
            for col in range(len(board)):
                save_num = board[row][col]
                if isinstance(board[row][col], int):
                    board[row][col] = self.get_mark()
                    position_weight = self.minimax(board, 0, False)
                    board[row][col] = save_num

                    if position_weight > best_weight:
                        best_position = (row, col)
                        best_weight = position_weight

        return board[best_position[0]][best_position[1]]

    def is_no_moves_made(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if not isinstance(board[row][col], int):
                    return False
        return True

    def is_moves_left(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if isinstance(board[row][col], int):
                    return True
        return False

    def evaluate(self, board):
        computer_player = "x"
        opponent = "o"
        size = len(board)

        for row in board:
            if all(cell == row[0] for cell in row):
                if row[0] == computer_player:
                    return 10
                elif row[0] == opponent:
                    return -10

        for col in range(size):
            if all(board[row][col] == board[0][col] for row in range(size)):
                if board[0][col] == computer_player:
                    return 10
                elif board[0][col] == opponent:
                    return -10

        if all(board[i][i] == board[0][0] for i in range(size)):
            if board[0][0] == computer_player:
                return 10
            elif board[0][0] == opponent:
                return -10

        if all(board[i][size - i - 1] == board[0][size - 1] for i in range(size)):
            if board[0][size - 1] == computer_player:
                return 10
            elif board[0][size - 1] == opponent:
                return -10

        return 0

    def minimax(self, board, depth, is_ai):
        score = self.evaluate(board)

        if score == 10:
            return score - depth

        if score == -10:
            return score + depth

        if not self.is_moves_left(board):
            return 0

        if is_ai:
            best = -1000
            for row in range(len(board)):
                for col in range(len(board)):
                    if isinstance(board[row][col], int):
                        save_num = board[row][col]

                        board[row][col] = 'x'

                        best = max(best, self.minimax(board, depth + 1, not is_ai))

                        board[row][col] = save_num
            return best
        else:
            best = 1000
            for row in range(len(board)):
                for col in range(len(board)):
                    if isinstance(board[row][col], int):
                        save_num = board[row][col]
                        board[row][col] = 'o'
                        best = min(best, self.minimax(board, depth + 1, not is_ai))
                        board[row][col] = save_num
            return best


