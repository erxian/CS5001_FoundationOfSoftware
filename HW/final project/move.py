'''
Zengping Xu
CS 5001, Fall 2020

This file defines everthing related to a move.
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
        '''
        Constructor -- creates a new instance of Move
            Parameters:
                self -- the current Move object
                start -- the start position of a piece
                end -- the end position of a piece
                is_capture -- if end position is a capture move
        '''
        self.start = start
        self.end = end
        self.is_capture = is_capture

    def __eq__(self, other):
        '''
        Method -- __eq__
            Checks if two objects are equal
        Parameters:
            self -- The Move object
            other -- An object to compare self to.
        Returns:
            True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.start == other.start and \
            self.end == other.end and \
                self.is_capture == other.is_capture