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
    square_row, square_col = coordinate_to_index(x, y)

    if game_state.game_over():
        print("Game Over")
        return

    if game_state.is_player(square_row, square_col):
        # if click a legal piece, highlight the piece's
        # square with blue line, highlight the available diagonal
        # square with red line
        game_state.selected_piece = (square_row, square_col)
        game_state.available_move = []
        game_state.available_capture = []
        game_state.check_diagonal(square_row, square_col)
        draw_canvas.highlight_square(game_state)
        game_state.is_select_piece = True
    
    if is_valid_move(square_row, square_col):
        # if last click select a legal piece, and next click select
        # the available diagonal square, then move the piece to the
        # diagonal square
        
        # determine if the piece become a king piece
        if game_state.current_piece.player == "BLACK" and square_row == 7:
            game_state.current_piece = black_king
            print("black become king")
        if game_state.current_piece.player == "RED" and square_row == 0:
            game_state.current_piece = red_king
            print("red become king")
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
        if is_capture_move(square_row, square_col):
            en_x = int((square_row + x) / 2)
            en_y = int((square_col + y) / 2)
            game_state.squares[en_x][en_y] = empty
        game_state.squares[x][y] = empty
        draw_canvas.update_square(game_state)
 
        if is_capture_move(square_row, square_col) and \
            not is_capture_end(square_row, square_col):
            # there are multiple capture, so need continue
            game_state.capture_continue = True
            # set (square_row, square_col) to selected_piece
            game_state.selected_piece = (square_row, square_col)
            # highlight the moved piece with blue
            # highlight the capture square with red
            draw_canvas.highlight_square(game_state)
            # restrict the next click must be the available_capture
            print("keep moving")
        else:
            if game_state.current_piece.player == "BLACK":
                game_state.current_piece = red_piece
            else:
                game_state.current_piece = black_piece
            game_state.is_select_piece = False
            game_state.capture_continue = False

    if not game_state.is_player(square_row, square_col) and \
        not is_valid_move(square_row, square_col) and \
        not game_state.capture_continue:
        # if not click a legal piece and not click the selected
        # diagonal either, then cancel the highlight squares
        draw_canvas.cancel_highlight(game_state)


def is_valid_move(square_row, square_col):
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
    if not game_state.is_select_piece:
        return False
    if len(game_state.available_capture) == 0:
        return (square_row, square_col) in game_state.available_move
    if len(game_state.available_capture) != 0:
        return (square_row, square_col) in game_state.available_capture


def is_capture_move(square_row, square_col):
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
    if not game_state.is_select_piece:
        return False
    return (square_row, square_col) in game_state.available_capture



def is_capture_end(square_row, square_col):
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
    game_state.available_move = []
    game_state.available_capture = []
    game_state.check_diagonal(square_row, square_col)
    if len(game_state.available_capture) == 0:
        return True
    return False


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
