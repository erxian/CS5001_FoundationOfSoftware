'''
Zengping Xu
CS 5001, Fall 2020

This file test everything related to the piece.
'''
from piece import Piece


def test_constructor():
    black_piece = Piece("BLACK", [[1, 1], [1, -1]], False)
    assert(black_piece.player == "BLACK")
    assert(black_piece.direction == [[1, 1], [1, -1]])
    assert(not black_piece.is_king)


def test_eq():
    red_king = Piece("RED", [[1, 1], [1, -1], [-1, 1], [-1, -1]], True)
    assert(red_king == Piece("RED", [[1, 1], [1, -1], [-1, 1], [-1, -1]], True))
    assert(red_king != Piece("BLACK", [[1, 1], [1, -1], [-1, 1], [-1, -1]], True))
    assert(red_king != "Red king")
