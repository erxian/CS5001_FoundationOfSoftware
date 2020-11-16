'''
Zengping Xu
CS 5001, Fall 2020

This code will get you started with the final project, milestone 1.
'''
import turtle


NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "white")
CIRCLE_COLORS = ("black", "brown")


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    board_size = NUM_SQUARES * SQUARE
    if abs(x) > board_size / 2 or abs(y) > board_size / 2:
        print("Clicked at", x, y, "not in a valid square on the board")
    else:
        print("Clicked at", x, y, "in a valid square on the board")


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


def main():
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. This should be the width of the board plus a little margin
    window_size = board_size + SQUARE # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white") # The window's background color
    turtle.tracer(0, 0) # makes the drawing appear immediately

    pen = turtle.Turtle() # This variable does the drawing.
    pen.penup() # This allows the pen to be moved.
    pen.hideturtle() # This gets rid of the triangle cursor.

    pen.color("black", "white") # The first parameter is the outline color, the second is the fille

    # YOUR CODE HERE
    pen.setposition(-board_size / 2, -board_size / 2)
    draw_square(pen, board_size)
    start = int(-board_size / 2)
    black_piece_col = 3  # black piece ends up with colunum 3
    red_piece_col = 4  # red piece start with 5
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if (row % 2) != (col % 2):   
                pen.setposition(start + SQUARE * row, start + SQUARE * col)
                pen.color("black", SQUARE_COLORS[0])
                draw_square(pen, SQUARE)
                pen.setposition(start + SQUARE * row + SQUARE / 2, start + SQUARE * col)
                if col < black_piece_col:
                    pen.color(SQUARE_COLORS[0], CIRCLE_COLORS[0])
                    draw_circle(pen, SQUARE / 2)
                if col > red_piece_col:
                    pen.color(SQUARE_COLORS[0], CIRCLE_COLORS[1])
                    draw_circle(pen, SQUARE / 2)

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler) # This will call call the click_handler function when a click occurs
    turtle.done() # Stops the window from closing.



if __name__ == "__main__":
    main()