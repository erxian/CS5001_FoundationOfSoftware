'''
Zengping Xu
CS 5001, Fall 2020

This code will make a graphical game of Checkers (AKA
Draughts), The game is played with black and red pieces
on an 8x8 board with light and dark squares in a checkerboard
pattern. The goal of the game is to capture all of your
opponent's pieces.
'''


class Piece:
    '''
    Class -- Piece
        Information about what the pieces
    Attributes:
        player --  black or red
        direction -- the direction it can move
        is_king -- if the piece is a king
    '''
    def __init__(self, player, direction, is_king):
        self.player = player
        self.direction = direction
        self.is_king = is_king
