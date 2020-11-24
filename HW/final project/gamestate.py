'''
'''
class GameState:
    '''
    Class -- GameState
        Information about what pieces are where on the board
        Rules e.g. about legal moves
        Whose turn it is
        Whether or not the game is over
    Attributes:
        squares -- collection storing piece locations
        current_player -- whose turn it is
        is_select_piece -- a boolean, if the last click selected a valid piece
        available_move -- a list, record the available move index
        available_kill -- a list, record the available kill index
        selected_piece -- a tuple, record the index of selected piece
    Methods:
        is_player -- check if click the current play's piece
        check_diagonal -- check the legal diagonal index of the selected piece
        game_over -- determine whether or not the game is over
    '''
    def __init__(self):
        self.squares = [
            ["EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK"],
            ["BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY"],
            ["EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK", "EMPTY", "BLACK"],
            ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
            ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
            ["RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY"],
            ["EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED"],
            ["RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY", "RED", "EMPTY"],
        ]
        self.current_player = "BLACK"
        self.is_select_piece = False
        self.available_move = []
        self.available_kill = []
        self.selected_piece = ()
        

    def is_player(self, row, col):
        '''
        Function -- is_player
            check if click the current play's piece
        Parameters:
            row -- the row index of squares
            col -- the col index of squares
        Returns:
            a boolean, True if click the right piece,
            False otherwise.
        '''
        return self.squares[row][col] == self.current_player


    def check_diagonal(self, row, col):
        '''
        Function -- check_diagonal
            find the legal diagonals of selected piece,
            record them into available_move
        Parameters:
            row -- the row index of squares
            col -- the col index of squares
        Returns:
            a list, each element represent the location
            of available move
        '''
        if self.current_player == "BLACK":
            try:
                if self.squares[row + 1][col - 1] == "EMPTY":
                    self.available_move.append((row + 1, col - 1))
                if self.squares[row + 1][col + 1] == "EMPTY":
                    self.available_move.append((row + 1, col + 1))
            except IndexError:
                print("index out of range")
                
        if self.current_player == "RED":
            try:
                if self.squares[row - 1][col + 1] == "EMPTY":
                    if row - 1 >= 0:
                        self.available_move.append((row - 1, col + 1))
                if self.squares[row - 1][col - 1] == "EMPTY":
                    if row - 1 >= 0 and col - 1 >= 0:
                        self.available_move.append((row - 1, col - 1))
            except IndexError:
                print("index out of range")
        return self.available_move


    def game_over(self):
        '''
        Function -- game_over
            determine whether or not the game is over,
            if one of the player has no pieces, game
            is over. Next version, when one of the player
            has no moveable pieces, game is over
        Parameters:
            no parameters
        Retruns:
            True if game over, False otherwise
        '''
        remain_black = False
        remain_red = False
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                if self.squares[row][col] == "BLACK":
                    remain_black = True
                if self.squares[row][col] == "RED":
                    remain_red = True
        return remain_black != remain_red
