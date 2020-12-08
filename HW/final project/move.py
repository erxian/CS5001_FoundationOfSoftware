'''
Zengping Xu
CS 5001, Fall 2020

This code will make a graphical game of Checkers (AKA
Draughts), The game is played with black and red pieces
on an 8x8 board with light and dark squares in a checkerboard
pattern. The goal of the game is to capture all of your
opponent's pieces.
'''


class Move:
    '''
    Class -- Move
        Information about what the pieces
    Attributes:
        start -- a start location, the square containing the 
                piece at the beginning of the move
        end -- an end location - the square that the moved piece ends up in
        is_capture -- whether or not it is a capturing move
    '''
    def __init__(self, start, end, is_capture):
        self.start = start
        self.end = end
        self.is_capture = is_capture
