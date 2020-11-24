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


# The number of squares on each row.
NUM_SQUARES = 8
# The size of each square in the checkerboard.
SQUARE = 50
SQUARE_COLORS = ("light gray", "white")
CIRCLE_COLORS = ("black", "brown")
game_state = GameState()
# Create the UI window. This should be the width
# of the board plus a little margin
board_size = NUM_SQUARES * SQUARE
start = int(-board_size / 2)


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
    if is_current_play(square_row, square_col):
        game_state.selected_piece = (square_row, square_col)
        game_state.available_move = []
        game_state.check_diagonal(square_row, square_col)
        highlight_square()
        game_state.is_select_piece = True
    
    if is_valid_move(square_row, square_col):
        game_state.squares[square_row][square_col] = game_state.current_player
        x = game_state.selected_piece[0]
        y = game_state.selected_piece[1]
        game_state.squares[x][y] = "EMPTY"
        update_square()


def is_current_play(square_row, square_col):
    '''
    '''
    result = False
    if game_state.is_player(square_row, square_col):
        result = True
    else:
        print(f"current is {game_state.current_player} return")
    return result


def is_valid_move(square_row, square_col):
    '''
    '''
    if not game_state.is_select_piece:
        return False
    return (square_row, square_col) in game_state.available_move


def highlight_square():
    '''
    '''
    new_pen = turtle.Turtle()
    new_pen.penup()
    new_pen.hideturtle()
    draw_checkboard(new_pen)
    draw_pieces(new_pen)
    draw_highlight(new_pen)


def update_square():
    '''
    '''
    new_pen = turtle.Turtle()
    new_pen.penup()
    new_pen.hideturtle()
    draw_checkboard(new_pen)
    draw_pieces(new_pen)
    if game_state.current_player == "BLACK":
        game_state.current_player = "RED"
    else:
        game_state.current_player = "BLACK"
    game_state.is_select_piece = False


def draw_checkboard(a_turtle):
    '''
    '''
    # The first parameter is the outline color,
    # the second is the fille
    a_turtle.color("black", "white")
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if (row % 2) != (col % 2):
                a_turtle.setposition(
                                start + SQUARE * row,
                                start + SQUARE * col)
                a_turtle.color("black", SQUARE_COLORS[0])
                draw_square(a_turtle, SQUARE)
                a_turtle.setposition(
                                start + SQUARE * row + SQUARE / 2,
                                start + SQUARE * col)


def draw_pieces(a_turtle):
    '''
    '''
    for row in range(NUM_SQUARES):
        for col in range(NUM_SQUARES):
            if game_state.squares[row][col] != "EMPTY":
                if game_state.squares[row][col] == "BLACK":
                    a_turtle.color(SQUARE_COLORS[0], CIRCLE_COLORS[0])
                if  game_state.squares[row][col] == "RED":
                    a_turtle.color(SQUARE_COLORS[0], CIRCLE_COLORS[1])                
                a_turtle.setposition(
                                    start + SQUARE * col + SQUARE / 2,
                                    start + SQUARE * row)
                draw_circle(a_turtle, SQUARE / 2)


def  draw_highlight(a_turtle):
    '''
    '''
    a_turtle.color("red", "light gray")
    for item in game_state.available_move:
        a_turtle.setposition(start + item[1] * SQUARE, start + item[0] * SQUARE)
        draw_square(a_turtle, SQUARE)


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.begin_fill()
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.penup()
    a_turtle.end_fill()


def draw_circle(a_turtle, radius):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.begin_fill()
    a_turtle.pendown()
    a_turtle.circle(radius)
    a_turtle.penup()
    a_turtle.end_fill()


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
    board_size = NUM_SQUARES * SQUARE
    square_col = int((x + board_size / 2) // SQUARE)
    square_row = int((y + board_size / 2) // SQUARE)
    return square_row, square_col


def main():
    # The extra + SQUARE is the margin
    window_size = board_size + SQUARE
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be
    # actual board size
    turtle.screensize(board_size, board_size)

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
    pen.setposition(-board_size / 2, -board_size / 2)

    # Step 1 - the board outline
    corner = -board_size / 2
    pen.setposition(corner, corner)
    draw_square(pen, board_size)
    
    # Step 2 - draw checkboard and pieces
    draw_checkboard(pen)
    draw_pieces(pen)

    # Click handling
    screen = turtle.Screen()
    # This will call call the click_handler function
    # when a click occurs
    screen.onclick(click_handler)
    # Stops the window from closing.
    turtle.done()


if __name__ == "__main__":
    main()
