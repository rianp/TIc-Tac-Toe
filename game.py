class Game:

    def play_round(self, board, players, console, validator):
        console.print_string(str(board))

        current_player = players.get_current_player()
        name = current_player.get_name()
        current_mark = current_player.get_mark()

        move_prompt = f'\nHi Player {name}! Enter a value please: '
        move = self.get_move(board, console, move_prompt, validator)

        self.update_game(board, current_mark, move, players)

        is_game_over = board.get_board_winner_status()
        if is_game_over:
            return self.get_message(is_game_over, players)

        return self.play_round(board, players, console, validator)

    def update_game(self, board, current_mark, move, players):
        board.update_board(current_mark, move)
        players.change_turn()

    def get_move(self, board, console, string, validator):
        user_move = console.prompt_input(string)
        is_valid, error_message = validator.validate_move(user_move, board)

        if is_valid:
            return int(user_move)

        try_again = f"{error_message}" \
                    f"\nIt's okay though! We'll try again! Enter a value please: "
        return self.get_move(board, console, try_again, validator)

    def get_message(self, is_game_over, players):

        if is_game_over is None:
            return "Eek! Looks like it's a tie friends. Goodbye."

        if is_game_over:
            winner = self.get_winner(players)
            return f"OMG! Congratulations Player {winner}, You won!"

        return ""

    def get_winner(self, players):
        players.change_turn()
        winner = players.get_current_player().get_name()
        return winner
