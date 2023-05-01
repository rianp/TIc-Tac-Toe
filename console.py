class Console:

    def print_string(self, string):
        print(string)

    def prompt_input(self, string):
        result = input(string)
        return result

    def print_greeting(self):
        return self.print_string("\n                         ᕙ(Ⓘ‿‿Ⓘ)ᕗ"
                                 "\n   <----** Hello friend! Welcome to Tic-Tac-Toe!!! **----> "
                                 )

    def print_instructions(self):
        return self.print_string(
            """    
*------------------------------------------------------------*
*           Here are the instructions to the game!           *
*------------------------------------------------------------*
* 1. there are two players in the game (X and O)             *
* 2. players can choose a 3x3 or a 5x5 board size            *
* 3. a player can take a field if not already taken          *
* 4. players take turns taking fields until the game is over *
* 5. a game is over when:                                    *
*   - all fields in a row are taken by a player              *
*   - all fields in a column are taken by a player           *
*   - all fields in a diagonal are taken by a player         *
*   - all fields are taken                                   *
*------------------------------------------------------------* 
        """
                               )

    def get_integer_input(self, prompt, validator):
        choice = self.prompt_input(prompt)
        validated_choice = validator(choice)

        if validated_choice.is_valid is True:
            return int(choice)

        try_again = f"{validated_choice.message}" \
                    f"\nIt's okay though! We'll try again! Make a selection please: "

        return self.get_integer_input(try_again, validator)

    def print_board(self, board):
        return self.print_string(self.format_board(board))

    def format_board(self, board):
        rows = []
        cells = "  |  ".join(["{}"] * len(board))
        max_num_len = len(str(len(board) * len(board)))
        padding = " " * 4

        for num in range(len(board)):
            row_nums = [str(elem).rjust(max_num_len) for elem in board[num]]
            row_str = cells.format(*row_nums)
            rows.append(f"*{padding}{row_str}{padding}*\n")

        divider = f"*{padding}{'-' * (len(rows[0]) - 11)}{padding}*\n"
        title = f"*{'Current Board'.center((len(rows[0]) - 3), ' ')}*\n"
        border = f"{'*' * (len(rows[0]) - 1)}\n"

        return "".join([border, title, border, divider.join(rows), border])
