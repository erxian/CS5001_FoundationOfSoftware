'''
Zengping Xu
CS 5001, Fall 2020

This code will make a graphical game of Checkers (AKA
Draughts), The game is played with black and red pieces
on an 8x8 board with light and dark squares in a checkerboard
pattern. The goal of the game is to capture all of your
opponent's pieces.
'''
from piece import Piece
from move import Move


black_piece = Piece("BLACK", [[1, 1], [1, -1]], False)
red_piece = Piece("RED", [[-1, 1], [-1, -1]], False)
empty = Piece("EMPTY", [], False)


class GameState:
    '''
    Class -- GameState
        Information about what pieces are where on the board
        Rules e.g. about legal moves
        Whose turn it is
        Whether or not the game is over
    Attributes:
        squares -- collection storing piece locations
        current_piece -- whose turn it is
        is_select_piece -- a boolean, if the last click selected a valid piece
        available_move -- a list, record the available move index
        available_kill -- a list, record the available kill index
        selected_piece -- a tuple, record the index of selected piece
    Methods:
        is_player -- check if click the current play's piece
        is_valid_move -- justify whether click the movable diagonal
        is_capture_move -- justify whether click the capture move
        is_capture_end -- check if there is other enemy piece can be
                        captures after last capture move
        enemy -- identify the enemy of current player
        game_over -- determine whether or not the game is over
        get_piece_moves -- find the legal diagonals of selected piece
        ai_possible_moves -- get all possible moves of AI
    '''
    def __init__(self):
        self.squares = [
            [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
            [black_piece, empty, black_piece, empty, black_piece, empty, black_piece, empty],
            [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [red_piece, empty, red_piece, empty, red_piece, empty, red_piece, empty],
            [empty, red_piece, empty, red_piece, empty, red_piece, empty, red_piece],
            [red_piece, empty, red_piece, empty, red_piece, empty, red_piece, empty],
        ]
        self.current_piece = black_piece
        self.you_win = True
        self.is_select_piece = False
        self.capture_continue = False
        self.available_move = []
        self.available_capture = []
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
        # if capture_continue is True, click any piece is illegal
        if self.capture_continue:
            return False
        return self.squares[row][col].player == self.current_piece.player

    def is_valid_move(self, square_row, square_col):
        '''
        Function -- is_valid_move
            justify whether click the movable diagonal
        Parameters:
            square_row -- an integer, the row index in checkboard
            square_col -- an integer, the col index in checkboard
        Returns:
            a boolean, True if click the movable diagonal,
            False otherwise
        '''
        if not self.is_select_piece:
            return False
        if len(self.available_capture) == 0:
            return (square_row, square_col) in self.available_move
        if len(self.available_capture) != 0:
            return (square_row, square_col) in self.available_capture

    def is_capture_move(self, square_row, square_col):
        '''
        Function -- is_capture_move
            justify whether click the capture move
        Parameters:
            square_row -- an integer, the row index in checkboard
            square_col -- an integer, the col index in checkboard
        Returns:
            a boolean, True if click the capture move,
            False otherwise 
        '''
        if not self.is_select_piece:
            return False
        return (square_row, square_col) in self.available_capture

    def is_capture_end(self, square_row, square_col):
        '''
        Function -- is_capture_end
            check if there is other enemy piece can be
            captures after first capture move
        Parameters:
            square_row -- an integer, the row index in checkboard
            square_col -- an integer, the col index in checkboard
        Returns:
            a boolean, True if there exists extra capture,
            False otherwise
        '''
        self.available_move, self.available_capture = \
            self.get_piece_moves(square_row, square_col)
        if len(self.available_capture) == 0:
            return True
        return False

    def ai_end(self, square_row, square_col):
        all_moves, capture_moves = \
            self.get_piece_moves(square_row, square_col)
        if len(capture_moves) == 0:
            return capture_moves
        else:
            return capture_moves[0]

    def enemy(self):
        '''
        Function -- enemy
            identify the enemy of current player, if current
            player is BLACK then the enemy is RED
        Parameters:
            no parameters
        Returns:
            a string
        '''
        if self.current_piece.player == "BLACK":
            return "RED"
        if self.current_piece.player == "RED":
            return "BLACK"

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
        remain_black_piece = False
        remain_red_piece = False
        black_able_move = []
        red_able_move = []
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                move_steps = self.get_piece_moves(row, col)
                if self.squares[row][col].player == "BLACK":
                    black_able_move += move_steps
                    remain_black_piece = True
                if self.squares[row][col].player == "RED":
                    red_able_move += move_steps
                    remain_red_piece = True
        if not remain_black_piece or len(black_able_move) == 0:
            self.you_win = False
            return True
        if not remain_red_piece or len(red_able_move) == 0:
            self.you_win = True
            return True
        return False

    def get_piece_moves(self, row, col):
        '''
        Function -- get_piece_moves
            find the legal diagonals of selected piece,
            record them into available_move
        Parameters:
            row -- the row index of squares
            col -- the col index of squares
        Returns:
            a list, each element represent the location
            of available move
        '''
        all_moves = []
        capture_moves = []
        for direction in self.squares[row][col].direction:
            move_row = row + direction[0]
            move_col = col + direction[1]
            if move_row >= 0 and move_row <= 7 and move_col >= 0 and move_col <= 7:
                if self.squares[move_row][move_col].player == "EMPTY":
                    all_moves.append((move_row, move_col))
                elif self.squares[move_row][move_col].player == self.enemy():
                    n_move_row = move_row + direction[0]
                    n_move_col = move_col + direction[1]
                    if n_move_row >= 0 and n_move_row <= 7 and n_move_col>= 0 and n_move_col <= 7:
                        if self.squares[n_move_row][n_move_col].player == "EMPTY":
                            all_moves.append((n_move_row, n_move_col))
                            capture_moves.append((n_move_row, n_move_col))
        return all_moves, capture_moves

    def ai_possible_moves(self):
        '''
        Function -- ai_possible_moves
            get all possible moves of AI
        Parameters:
            no parameters
        Returns:
            a list, every element is a Move object
        '''
        ai_available_move = []  # every element is a Move object
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                if self.squares[row][col].player == "RED":
                    all_moves, capture_moves = self.get_piece_moves(row, col)
                    if len(all_moves) != 0:
                        if len(capture_moves) != 0:
                            pick_move = capture_moves[0]
                            is_cap = True
                        else:
                            pick_move = all_moves[0]
                            is_cap = False
                        move_obj = Move((row, col), pick_move, is_cap)
                        ai_available_move.append(move_obj)
        return ai_available_move
