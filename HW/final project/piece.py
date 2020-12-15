'''
Zengping Xu
CS 5001, Fall 2020

This file defines everthing related to a piece.
'''


class Piece:
    '''
    Class -- Piece
        Information about what the pieces
    Attributes:
        player --  the current player, BLACK or Red
        direction -- the current player, BLACK or Red
        is_king -- if the piece is a king
    '''
    def __init__(self, player, direction, is_king):
        '''
            Constructor -- creates a new instance of Piece
            Parameters:
                self -- the current Piece object
                player -- the current player, BLACK or Red
                direction -- the direction a piece can move
                is_king -- if a piece is king
        '''
        self.player = player
        self.direction = direction
        self.is_king = is_king

    def __eq__(self, other):
        '''
        Method -- __eq__
            Checks if two objects are equal
        Parameters:
            self -- The Piece object
            other -- An object to compare self to.
        Returns:
            True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.player == other.player and \
            self.direction == other.direction and \
                self.is_king == other.is_king