class Validator:
    @staticmethod
    def is_on_board(choice, board):
        return any(choice in row for row in board)

    @staticmethod
    def is_in_range(choice, board_range):
        return choice in board_range

    @staticmethod
    def is_valid_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    def validate_size(self, size):
        if not self.is_valid_integer(size):
            return ValidationResult(False, "Eek! That's not even a number! ")

        if not self.is_in_range(int(size), range(3, 6)):
            return ValidationResult(False, "Whoa friend! This is outta bounds! ")

        if not self.is_odd(int(size)):
            return ValidationResult(False, "Ummm. This isn't odd friend!")

        return ValidationResult(True, "")

    def validate_choice(self, choice):
        if not self.is_valid_integer(choice):
            return ValidationResult(False, "Eek! That's not even a number! ")

        if not self.is_in_range(int(choice), range(1, 3)):
            return ValidationResult(False, "Whoa friend! This is outta bounds! ")

        return ValidationResult(True, "")


class ValidationResult:
    def __init__(self, boolean, string):
        self.is_valid = boolean
        self.message = string
