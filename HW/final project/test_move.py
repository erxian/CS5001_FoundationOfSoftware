'''
Zengping Xu
CS 5001, Fall 2020

This file test everything related to the move.
'''
from move import Move


def test_constructor():
    one_move = Move((4, 6), (3, 7), False)
    assert(one_move.start == (4, 6))
    assert(one_move.end == (3, 7))
    assert(not one_move.is_capture)


def test_eq():
    a_move = Move((4, 6), (3, 7), False)
    assert(a_move == Move((4, 6), (3, 7), False))
    assert(a_move != Move((2, 2), (3, 3), False))
    assert(a_move != "Piece Move")
