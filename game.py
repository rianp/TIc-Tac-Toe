from board import WinnerStatus


class Game:

    def __init__(self, board, players, console, validator):
        self.board = board
        self.players = players
        self.console = console
        self.validator = validator

    def play_round(self):
        board = self.board
        players = self.players
        console = self.console

        console.print_board(board.get_board())

        current_player = players.get_current_player()
        name = current_player.get_name()
        current_mark = current_player.get_mark()

        move_prompt = f'\nHi Player {name}! Enter a value please: '
        move = self.get_move(move_prompt)

        self.update_game(current_mark, move)

        is_game_over = board.get_board_winner_status()
        if is_game_over is not WinnerStatus.ONGOING:
            return self.get_message(is_game_over)

        return self.play_round()

    def update_game(self, current_mark, move):
        board = self.board
        players = self.players

        board.update_board(current_mark, move)
        players.change_turn()

    def get_move(self, string):
        console = self.console

        user_move = console.prompt_input(string)
        is_valid = self.validate_move(user_move)

        if is_valid == int(user_move):
            return int(user_move)

        try_again = f"{is_valid}" \
                    f"\nIt's okay though! We'll try again! Enter a value please: "
        return self.get_move(try_again)

    def validate_move(self, user_input):
        board = self.board
        validator = self.validator

        if not validator.is_valid_integer(user_input):
            return "Eek! That's not even a number! "

        if not validator.is_in_range(int(user_input), board.get_board_range()):
            return "Whoa friend! This is outta bounds! "

        if not validator.is_on_board(int(user_input), board.get_board()):
            return "Rats! Someone already snagged this one! "

        return int(user_input)

    def get_message(self, is_game_over):
        if is_game_over is WinnerStatus.DRAW:
            return "Eek! Looks like it's a tie friends. Goodbye."

        winner = self.get_winner()
        return f"OMG! Congratulations Player {winner}, You won!"

    def get_winner(self):
        players = self.players

        players.change_turn()
        winner = players.get_current_player().get_name()
        return winner
