from board import WinnerStatus


class Game:

    def __init__(self, board, players, console, validator):
        self.board = board
        self.players = players
        self.console = console
        self.validator = validator

    def play_round(self):
        self.console.print_board(self.board.get_board())
        current_player = self.players.get_current_player()
        name = current_player.get_name()
        current_mark = current_player.get_mark()

        if name == "Bot":
            move = current_player.make_move(self.board.get_board())
        elif name == "Super Bot":
            self.console.print_string("Watch in awe as Super Player Bot makes a really impressive move!")
            move = current_player.make_move(self.board.get_board())
        else:
            move_prompt = f'\nHi Player {name}! Enter a value please: '
            move = self.get_move(move_prompt)

        self.update_game(current_mark, move)

        is_game_over = self.board.get_board_winner_status()
        if is_game_over is not WinnerStatus.ONGOING:
            return self.get_message(is_game_over)

        return self.play_round()

    def update_game(self, current_mark, move):
        self.board.update_board(current_mark, move)
        self.players.change_turn()

    def get_move(self, string):
        user_move = self.console.prompt_input(string)
        is_valid = self.validate_move(user_move)

        if is_valid == int(user_move):
            return int(user_move)

        try_again = f"{is_valid}" \
                    f"\nIt's okay though! We'll try again! Enter a value please: "
        return self.get_move(try_again)

    def validate_move(self, user_input):
        if not self.validator.is_valid_integer(user_input):
            return "Eek! That's not even a number! "

        if not self.validator.is_in_range(int(user_input), self.board.get_board_range()):
            return "Whoa friend! This is outta bounds! "

        if not self.validator.is_on_board(int(user_input), self.board.get_board()):
            return "Rats! Someone already snagged this one! "

        return int(user_input)

    def get_message(self, is_game_over):
        if is_game_over is WinnerStatus.DRAW:
            return "Eek! Looks like it's a tie friends. Goodbye."

        winner = self.get_winner()
        return f"OMG! Congratulations Player {winner}, You won!"

    def get_winner(self):
        self.players.change_turn()
        winner = self.players.get_current_player().get_name()
        return winner
