class Game:

    def play_round(self, board, players, console, validator):
        game_status = self.is_game_over(board)

        if not self.display_game_status(game_status, players, console, board):
            return

        current_player = players.get_current_player().get_name()
        move_prompt = f'\nHi Player {current_player}! Enter a value please: '
        move = self.get_move(board, console, move_prompt, validator)
        self.update_game(players, move, board)

        return self.play_round(board, players, console, validator)

    def update_game(self, players, move, board):
        player_mark = players.get_current_player().get_mark()
        board.update_board(player_mark, move)
        players.change_turn()

    def get_move(self, board, console, string, validator):
        user_move = console.prompt_input(string)

        if validator.validate_move(user_move, board, console):
            return int(user_move)
        else:
            try_again = "\nIt's okay though! We'll try again! Enter a value please: "
            return self.get_move(board, console, try_again, validator)

    def display_game_status(self, game_status, players, console, board):
        if game_status is None:
            console.print_string("Eek! Looks like it's a tie friends. Goodbye.")
            return False

        if game_status:
            players.change_turn()
            winner = players.get_current_player()
            string = f"OMG! Congratulations Player {winner.get_name()}, You won!"
            console.print_string(string)
            return False

        if not game_status:
            console.print_string(str(board))
            return True

    def is_game_over(self, board):
        return board.get_board_state()
