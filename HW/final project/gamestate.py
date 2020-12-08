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
        check_diagonal -- check the legal diagonal index of the selected piece
        game_over -- determine whether or not the game is over
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
        for direction in self.squares[row][col].direction:
            move_row = row + direction[0]
            move_col = col + direction[1]
            if move_row >= 0 and move_row <= 7 and move_col >= 0 and move_col <= 7:
                if self.squares[move_row][move_col].player == "EMPTY":
                    self.available_move.append((move_row, move_col))
                elif self.squares[move_row][move_col].player == self.enemy():
                    n_move_row = move_row + direction[0]
                    n_move_col = move_col + direction[1]
                    if n_move_row >= 0 and n_move_row <= 7 and n_move_col>= 0 and n_move_col <= 7:
                        if self.squares[n_move_row][n_move_col].player == "EMPTY":
                            self.available_move.append((n_move_row, n_move_col))
                            self.available_capture.append((n_move_row, n_move_col))


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
        remain_black = False
        remain_red = False
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                if self.squares[row][col].player == "BLACK":
                    remain_black = True
                if self.squares[row][col].player == "RED":
                    remain_red = True
        return remain_black != remain_red
