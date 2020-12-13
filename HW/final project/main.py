'''
Zengping Xu
CS 5001, Fall 2020

This code will make a graphical game of Checkers (AKA
Draughts), The game is played with black and red pieces
on an 8x8 board with light and dark squares in a checkerboard
pattern. The goal of the game is to capture all of your
opponent's pieces.
'''
import turtle
from gamestate import GameState
from drawcanvas import DrawCanvas
from piece import Piece


draw_canvas = DrawCanvas()
game_state = GameState()
empty = Piece("EMPTY", [], False)
black_piece = Piece("BLACK", [[1, 1], [1, -1]], False)
red_piece = Piece("RED", [[-1, 1], [-1, -1]], False)
black_king = Piece("BLACK", [[1, 1], [1, -1], [-1, 1], [-1, -1]], True)
red_king = Piece("RED", [[1, 1], [1, -1], [-1, 1], [-1, -1]], True)


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically
                provided by Turtle.
            y -- Y coordinate of the click. Automatically
                provided by Turtle.
        Returns:
            Does not and should not return. Click handlers
            are a special type of function automatically
            called by Turtle. You will not have access to
            anything returned by this function.
    '''
    if game_state.game_over():
        return
    square_row, square_col = coordinate_to_index(x, y)
    # if click a legal piece, highlight the piece's
    # square with blue line, highlight the available diagonal
    # square with red line
    if game_state.is_player(square_row, square_col):
        game_state.selected_piece = (square_row, square_col)
        game_state.available_move = []
        game_state.available_capture = []
        # get the piece's available move and capture move
        game_state.available_move, game_state.available_capture = \
            game_state.get_piece_moves(square_row, square_col)
        draw_canvas.highlight_square(game_state)
        game_state.is_select_piece = True
    # if last click select a legal piece, and next click select
    # the available diagonal square, then move the piece to the
    # diagonal square
    if game_state.is_valid_move(square_row, square_col):
        # determine if the piece become a king piece
        if game_state.current_piece.player == "BLACK" and square_row == 7:
            game_state.current_piece = black_king
        # convert selected piece's index
        x = game_state.selected_piece[0]
        y = game_state.selected_piece[1]
        if game_state.squares[x][y].is_king == True:
            # move selected piece(king piece) to new position
            game_state.squares[square_row][square_col] = game_state.squares[x][y]
        else:
            # move current piece(regular piece) to new positon
            game_state.squares[square_row][square_col] = game_state.current_piece
        # if there exists capture move, must make this capture, and
        # remove enemy's pieces from index square[en_x][en_y]
        if game_state.is_capture_move(square_row, square_col):
            en_x = int((square_row + x) / 2)
            en_y = int((square_col + y) / 2)
            game_state.squares[en_x][en_y] = empty
        game_state.squares[x][y] = empty
        draw_canvas.update_square(game_state)
 
        if game_state.is_capture_move(square_row, square_col) and \
            not game_state.is_capture_end(square_row, square_col):
            # there are multiple capture, so need continue
            game_state.capture_continue = True
            # set (square_row, square_col) to selected_piece
            game_state.selected_piece = (square_row, square_col)
            # highlight the moved piece with blue
            # highlight the capture square with red
            draw_canvas.highlight_square(game_state)
            # after every move, check if game over
        else:
            # finish this turn and switch to the opponent
            if game_state.current_piece.player == "BLACK":
                game_state.current_piece = red_piece
                if game_state.game_over():
                    draw_canvas.end_sign(game_state)
                    return
                ai_move()  # AI's turn
                if game_state.game_over():
                    draw_canvas.end_sign(game_state)
                    return
            game_state.is_select_piece = False
            game_state.capture_continue = False
    # if not click a legal piece and not click the selected
    # diagonal either, then cancel the highlight squares
    if not game_state.is_player(square_row, square_col) and \
        not game_state.is_valid_move(square_row, square_col) and \
        not game_state.capture_continue:
        draw_canvas.cancel_highlight(game_state)


def ai_move():
    capture = False
    # Get all possible moves for the AI and keep them in a list
    ai_available_move = game_state.ai_possible_moves()
    # Pick a move from the list. if a move is capture move, then
    # ai's next move is the capture move. if there is no capture
    # move, then pick the first move in the list
    for move in ai_available_move:
        if move.is_capture:
            capture = True
            next_move = move
    if not capture:
        next_move = ai_available_move[0]

    start_x = next_move.start[0]
    start_y = next_move.start[1]
    end_x = next_move.end[0]
    end_y = next_move.end[1]
    if game_state.current_piece.player == "RED" and end_x == 0:
        game_state.current_piece = red_king
    if game_state.squares[start_x][start_y].is_king == True:
        # move selected piece(king piece) to new position
        game_state.squares[end_x][end_y] = game_state.squares[start_x][start_y]
    else:
        # move current piece(regular piece) to new positon
        game_state.squares[end_x][end_y] = game_state.current_piece
    if capture:
        enemy_x = int((start_x + end_x) / 2)
        enemy_y = int((start_y + end_y) / 2)
        game_state.squares[enemy_x][enemy_y] = empty
    game_state.squares[start_x][start_y] = empty
    draw_canvas.update_square(game_state)
    if capture:
        # when there is multiple capture, keep capturing
        while len(game_state.ai_end(end_x, end_y)) != 0:
            extra_move = game_state.ai_end(end_x, end_y)
            if game_state.current_piece.player == "RED" and extra_move[0] == 0:
                game_state.current_piece = red_king
            if game_state.squares[end_x][end_y].is_king == True:
                # move selected piece(king piece) to new position
                game_state.squares[extra_move[0]][extra_move[1]] = \
                    game_state.squares[end_x][end_y]
            else:
                # move current piece(regular piece) to new positon
                game_state.squares[extra_move[0]][extra_move[1]] = \
                    game_state.current_piece
            enemy_x = int((end_x + extra_move[0]) / 2)
            enemy_y = int((end_y + extra_move[1]) / 2)
            game_state.squares[enemy_x][enemy_y] = empty
            game_state.squares[end_x][end_y] = empty
            draw_canvas.update_square(game_state)
            end_x = extra_move[0]
            end_y = extra_move[1]
    # finish this turn and switch to the opponent
    game_state.current_piece = black_piece


def coordinate_to_index(x, y):
    '''
    Function -- coordinate_to_index
        convert x, y coordinate to squares index
    Parameters:
        x -- a float, represent x coordinate
        y -- a float, represent y coordinate
    Returns:
        two integer, which are corespound to the
        location in squares
    '''
    square_col = int((x + draw_canvas.board_size / 2) // draw_canvas.SQUARE)
    square_row = int((y + draw_canvas.board_size / 2) // draw_canvas.SQUARE)
    return square_row, square_col


def main():
    # The extra + SQUARE is the margin
    window_size = draw_canvas.board_size + draw_canvas.SQUARE
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be
    # actual board size
    turtle.screensize(draw_canvas.board_size, draw_canvas.board_size)

    # The window's background color
    turtle.bgcolor("white")
    turtle.tracer(0, 0)

    # This variable does the drawing.
    pen = turtle.Turtle()

    # This allows the pen to be moved.
    pen.penup()

    # This gets rid of the triangle cursor.
    pen.hideturtle()
    pen.color("black", "white")
    pen.setposition(-draw_canvas.board_size / 2, -draw_canvas.board_size / 2)

    # Step 1 - the board outline
    corner = -draw_canvas.board_size / 2
    pen.setposition(corner, corner)
    draw_canvas.draw_square(pen, draw_canvas.board_size)
    
    # Step 2 - draw checkboard and pieces
    draw_canvas.draw_checkboard(pen)
    draw_canvas.draw_pieces(pen, game_state)

    # Click handling
    screen = turtle.Screen()
    # This will call call the click_handler function
    # when a click occurs
    screen.onclick(click_handler)
    # Stops the window from closing.
    turtle.done()


if __name__ == "__main__":
    main()
