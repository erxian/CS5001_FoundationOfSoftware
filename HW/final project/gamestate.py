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
    Methods:
        click
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
        

    def is_player(self, square_row, square_col):
        '''
        '''
        print("click", self.squares[square_row][square_col], "current", self.current_player)
        return self.squares[square_row][square_col] == self.current_player

    def check_diagonal(self, square_row, square_col):
        # square_row >= 0 and square_row < 8, square_col >= 0, and square_col < 8 (0, 1, 2, 3, 4, 5, 5, 7)
        if self.current_player == "BLACK":
            if (square_row + 1) < 8 and (square_col - 1) >= 0 and self.squares[square_row + 1][square_col - 1] == "EMPTY":
                self.available_move.append((square_col - 1, square_row + 1))
            if (square_row + 1) < 8 and (square_col + 1) < 8 and self.squares[square_row + 1][square_col + 1] == "EMPTY":
                self.available_move.append((square_col + 1, square_row + 1))
        if self.current_player == "RED":
            if (square_row - 1) >= 0 and (square_col + 1) < 8 and self.squares[square_row - 1][square_col + 1] == "EMPTY":
                self.available_move.append((square_col + 1, square_row - 1))
            if (square_row - 1) >= 0 and (square_col - 1) >= 0 and self.squares[square_row - 1][square_col - 1] == "EMPTY":
                self.available_move.append((square_col - 1, square_row - 1))
        return self.available_move

        

