class GameStart:

    def start_game(self):
        greeting = self.greeting()
        instructions = self.instructions()
        return greeting + instructions

    def greeting(self):
        return "\n                         ᕙ(Ⓘ‿‿Ⓘ)ᕗ"\
               "\n   <----** Hello friend! Welcome to Tic-Tac-Toe!!! **----> "

    def instructions(self):
        message = """    
*------------------------------------------------------------*
*           Here are the instructions to the game!           *
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
        return message
