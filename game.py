class Game:

    def play_round(self, board, players, console, validator):
        console.print_string(str(board))

        current_player = players.get_current_player().get_name()
        move_prompt = f'\nHi Player {current_player}! Enter a value please: '
        move = self.get_move(board, console, move_prompt, validator)

        mark = current_player().get_mark()
        board.update_board(mark, move)

        game_is_won = self.is_game_over(board)

        if game_is_won is None:
            return "Eek! Looks like it's a tie friends. Goodbye."

        if game_is_won:
            return f"OMG! Congratulations Player {current_player}, You won!"

        players.change_turn()

        return self.play_round(board, players, console, validator)

    def get_move(self, board, console, string, validator):
        user_move = console.prompt_input(string)
        is_valid, error_message = validator.validate_move(user_move, board)

        if is_valid:
            return int(user_move)
        else:
            try_again = f"{error_message}\nIt's okay though! We'll try again! Enter a value please: "
            return self.get_move(board, console, try_again, validator)

    def is_game_over(self, board):
        return board.get_board_state()
