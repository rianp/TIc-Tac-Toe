
class Validation:
    """ Validates user inputs and search results. """

    @staticmethod
    def validate_selection(choice, board):
        """ Validates number selection. """
        for row in board:
            if int(choice) in row:
                return True
        return False

