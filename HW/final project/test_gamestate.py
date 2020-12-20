'''
Zengping Xu
CS 5001, Fall 2020

This file test everything related to the game state.
'''
from gamestate import GameState
from piece import Piece
from move import Move


black_piece = Piece("BLACK", [[1, 1], [1, -1]], False)
red_piece = Piece("RED", [[-1, 1], [-1, -1]], False)
empty = Piece("EMPTY", [], False)


def test_constructor():
    game = GameState()
    squares = [
        [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
        [black_piece, empty, black_piece, empty, black_piece, empty, black_piece, empty],
        [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
        [empty, empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty, empty],
        [red_piece, empty, red_piece, empty, red_piece, empty, red_piece, empty],
        [empty, red_piece, empty, red_piece, empty, red_piece, empty, red_piece],
        [red_piece, empty, red_piece, empty, red_piece, empty, red_piece, empty],
    ]
    assert(game.squares == squares)
    assert(game.current_piece == black_piece)
    assert(game.human_win)
    assert(not game.is_select_piece)
    assert(not game.capture_continue)
    assert(game.available_move == [])
    assert(game.available_capture == [])
    assert(game.selected_piece == ())



def test_is_player():
    game = GameState()
    assert(game.is_player(0, 1))
    assert(not game.is_player(2, 2))


def test_is_valid_move():
    game = GameState()
    game.is_select_piece = True
    game.available_move = [(1, 0), (3, 4)]
    game.available_capture = [(3, 4)]
    assert(not game.is_valid_move(2, 2))
    assert(not game.is_valid_move(1, 0))
    assert(game.is_valid_move(3, 4))


def test_is_capture_move():
    game = GameState()
    game.is_select_piece = True
    game.available_capture = [(3, 0), (3, 4)]
    assert(game.is_capture_move(3, 0))
    assert(not game.is_capture_move(2, 1))


def test_is_capture_end():
    game = GameState()
    squares = [
            [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
            [black_piece, empty, black_piece, empty, black_piece, empty, black_piece, empty],
            [empty, black_piece, empty, empty, empty, black_piece, empty, black_piece],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, red_piece, empty, red_piece, empty, empty, empty, empty],
            [empty, empty, red_piece, empty, empty, empty, red_piece, empty],
            [empty, red_piece, empty, red_piece, red_piece, red_piece, empty, red_piece],
            [red_piece, empty, red_piece, empty, red_piece, empty, empty, empty],
    ]
    game.squares = squares
    assert(game.is_capture_end(2, 5))
    assert(not game.is_capture_end(3, 2))


def test_ai_capture_move():
    game = GameState()
    squares = [
            [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
            [black_piece, empty, black_piece, empty, black_piece, empty, black_piece, empty],
            [empty, black_piece, empty, empty, empty, black_piece, empty, black_piece],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, red_piece, empty, red_piece, empty, empty, empty, empty],
            [empty, empty, red_piece, empty, empty, empty, red_piece, empty],
            [empty, red_piece, empty, red_piece, red_piece, red_piece, empty, red_piece],
            [red_piece, empty, red_piece, empty, red_piece, empty, empty, empty],
    ]
    game.squares = squares
    game.current_piece = red_piece
    assert(game.ai_capture_move(4, 3) == [])
    assert(game.ai_capture_move(4, 1) == (2, 3))


def test_enemy():
    game = GameState()
    assert(game.enemy() == "RED")
    game.current_piece = red_piece
    assert(game.enemy() == "BLACK")


def test_eliminate_enemy():
    game = GameState()
    assert(not game.eliminate_enemy())
    no_red_squares = [
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, black_piece, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
    ]
    game.squares = no_red_squares
    assert(game.eliminate_enemy())


def test_keep_move():
    game = GameState()
    assert(game.keep_move)
    no_move_squares = [
            [empty, empty, empty, empty, empty, black_piece, empty, empty],
            [empty, empty, empty, empty, empty, empty, black_piece, empty],
            [empty, empty, empty, empty, empty, black_piece, empty, red_piece],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
    ]
    game.current_piece = red_piece
    game.squares = no_move_squares
    assert(not game.keep_move())


def test_get_piece_moves():
    game = GameState()
    squares = [
            [empty, black_piece, empty, black_piece, empty, black_piece, empty, black_piece],
            [black_piece, empty, black_piece, empty, black_piece, empty, black_piece, empty],
            [empty, black_piece, empty, empty, empty, black_piece, empty, black_piece],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, red_piece, empty, empty, empty, empty, empty, empty],
            [empty, empty, red_piece, empty, empty, empty, red_piece, empty],
            [empty, red_piece, empty, red_piece, red_piece, red_piece, empty, red_piece],
            [red_piece, empty, red_piece, empty, red_piece, empty, empty, empty],
    ]
    game.squares = squares
    assert(game.get_piece_moves(3, 2) == ([(4, 3), (5, 0)], [(5, 0)]))
    assert(game.get_piece_moves(2, 5) ==([(3, 6), (3, 4)], []))


def test_ai_possible_moves():
    game = GameState()
    squares = [
            [empty, empty, empty, empty, empty, black_piece, empty, empty],
            [empty, empty, empty, empty, empty, empty, black_piece, empty],
            [empty, empty, empty, empty, empty, black_piece, empty, red_piece],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, red_piece, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, black_piece, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty],
    ]
    game.squares = squares
    ai_move = Move((4, 6), (3, 7), False)
    assert(game.ai_possible_moves() == [ai_move])
