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
        self.selected_piece = ()
        

    def is_player(self, row, col):
        '''
        '''
        return self.squares[row][col] == self.current_player

    def check_diagonal(self, square_row, square_col):
        '''
        '''
        if self.current_player == "BLACK":
            try:
                if self.squares[square_row + 1][square_col - 1] == "EMPTY":
                    self.available_move.append((square_row + 1, square_col - 1))
                if self.squares[square_row + 1][square_col + 1] == "EMPTY":
                    self.available_move.append((square_row + 1, square_col + 1))
            except IndexError:
                print("index out of range")
                
        if self.current_player == "RED":
            try:
                if self.squares[square_row - 1][square_col + 1] == "EMPTY":
                    self.available_move.append((square_row - 1, square_col + 1))
                if self.squares[square_row - 1][square_col - 1] == "EMPTY":
                    self.available_move.append((square_row - 1, square_col - 1))
            except IndexError:
                print("index out of range")
        return self.available_move
