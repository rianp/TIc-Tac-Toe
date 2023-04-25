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

    def select_board_size(self, prompt, validator):
        size = self.prompt_input(prompt)
        validated_size = validator.validate_size(size)

        if validated_size.is_valid is True:
            return int(size)

        try_again = f"{validated_size.message}" \
                    f"\nIt's okay though! We'll try again! Enter an odd integer please: "

        return self.select_board_size(try_again, validator)

    def print_board(self, board):
        formatter = Formatter(board)
        return formatter.build_layout()


class Formatter:
    def __init__(self, board):
        self.board = board

    def build_layout(self):
        size = len(self.board)
        board = self.build_board_layout(size)
        width = self.calc_board_width(board)
        header = self.build_header(width)
        footer = self.build_footer(width)
        print(header + board + footer)
        return header + board + footer

    def build_board_layout(self, size):
        rows = []
        cells = "  |  ".join(["{}"] * size)
        max_num_len = len(str(size * size))
        padding = " " * 4

        for num in range(size):
            row_nums = [str(elem).rjust(max_num_len) for elem in self.board[num]]
            row_str = cells.format(*row_nums)
            rows.append(f"*{padding}{row_str}{padding}*\n")

        divider = f"*{padding}{'-' * (len(rows[0]) - 11)}{padding}*\n"

        return divider.join(rows)

    def build_header(self, width):
        title = "Current Board!"
        padding = " " * (((width - len(title)) // 2) - 1)
        line = f"{'*' * width}\n"

        return f"{line}*{padding}{title}{padding}*\n{line}"

    def build_footer(self, width):
        return f"{'*' * width}\n"

    def calc_board_width(self, string):
        counting = False
        count = 0

        for char in string:
            if char == "*":
                if not counting:
                    counting = True
                else:
                    break
            elif counting:
                count += 1

        return count + 2
