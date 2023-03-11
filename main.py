"""
This module contains the `main` function that creates any
necessary objects and calls functions to execute the program's logic.
"""
from console import *
from board import *


def main():
    """ Creates any necessary objects and calls functions to execute the program's logic. """
    game = Board()
    Console.print_string("Hello friend, welcome to Tic-Tac-Toe!")

    message = """
*------------------------------------------------------------*  
* Here are the instructions to the game!                     *
*------------------------------------------------------------*
* 1. there are two players in the game (X and O)             *
* 2. a game has nine fields in a 3x3 grid                    *
* 3. a player can take a field if not already taken          *
* 4. players take turns taking fields until the game is over *
* 5. a game is over when:                                    *
*   - all fields in a row are taken by a player              *
*   - all fields in a column are taken by a player           *
*   - all fields in a diagonal are taken by a player         *
*   - all fields are taken                                   *
*------------------------------------------------------------* 
"""

    Console.print_string(message)
    Console.print_string(str(game))


if __name__ == "__main__":
    main()
