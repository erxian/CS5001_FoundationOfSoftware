'''
Zengping Xu
CS 5001, Fall 2020

This code will get you started with the final project, milestone 1.
'''
import turtle


NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
STAR_COLORS = ("green", "blue", "dark orange", "red", "yellow")
count = 5 # The number of star line colors


def draw_star(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    L_ANGLE = 72
    R_ANGLE = 144
    a_turtle.pendown()
    step = 20
    # Draw the shortest green line
    a_turtle.color(STAR_COLORS[0])
    a_turtle.left(L_ANGLE)
    a_turtle.forward(size)
    # Draw the star's remaining side, the side gets longer and longer
    for i in range(1, 18):
        a_turtle.color(STAR_COLORS[i % count])
        a_turtle.right(R_ANGLE)
        a_turtle.forward(size + step * i)
    a_turtle.penup()


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

    # pen.color("black", "white") # The first parameter is the outline color, the second is the fille

    # YOUR CODE HERE
    pen.setposition(0, 0)
    draw_star(pen, 50)
    turtle.done()


if __name__ == "__main__":
    main()
