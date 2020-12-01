'''
'''
import turtle

class DrawCanvas:
    '''
    '''
    def __init__(self):
        self.NUM_SQUARES = 8
        self.SQUARE = 50
        self.SQUARE_COLORS = ("light gray", "white")
        self.CIRCLE_COLORS = ("black", "brown")
        self.board_size = self.NUM_SQUARES * self.SQUARE
        self.start = int(-self.board_size / 2)

    def highlight_square(self, game_state):
        '''
        Funtion -- highlight_square
            highlight the selected piece and the legal diagonals
        Parameters:
            does not need parameters
        Returns:
            Nothing
        '''
        new_pen = turtle.Turtle()
        new_pen.penup()
        new_pen.hideturtle()
        self.draw_checkboard(new_pen)
        self.draw_highlight(new_pen, game_state)
        self.draw_pieces(new_pen, game_state)

    def update_square(self, game_state):
        '''
        Funtion -- update_squares
            move the piece to its diagonal, and change
            the players turn
        Parameters:
            does not need parameters
        Returns:
            Nothing
        '''
        new_pen = turtle.Turtle()
        new_pen.penup()
        new_pen.hideturtle()
        self.draw_checkboard(new_pen)
        self.draw_pieces(new_pen, game_state)
        if game_state.current_player == "BLACK":
            game_state.current_player = "RED"
        else:
            game_state.current_player = "BLACK"
        game_state.is_select_piece = False

    def cancel_highlight(self, game_state):
        '''
        Function -- cancel_highlight
            cancel the highligth squares
        Parameters:
            does not need parameters
        Returns:
            Nothing.
        '''
        new_pen = turtle.Turtle()
        new_pen.penup()
        new_pen.hideturtle()
        self.draw_checkboard(new_pen)
        self.draw_pieces(new_pen, game_state)


    def draw_checkboard(self, a_turtle):
        '''
        Function -- draw_checkboard
            draw a 8x8 checkboard
        Parameters:
            a_turtle -- an instance of Turtle
        Returns:
            Nothing. Draws a square in the graphics window.
        '''
        # The first parameter is the outline color,
        # the second is the fille
        a_turtle.color("black", "white")
        for col in range(self.NUM_SQUARES):
            for row in range(self.NUM_SQUARES):
                if (row % 2) != (col % 2):
                    a_turtle.setposition(
                                    self.start + self.SQUARE * row,
                                    self.start + self.SQUARE * col)
                    a_turtle.color("black", self.SQUARE_COLORS[0])
                    self.draw_square(a_turtle, self.SQUARE)
                    a_turtle.setposition(
                                    self.start + self.SQUARE * row + self.SQUARE / 2,
                                    self.start + self.SQUARE * col)


    def draw_pieces(self, a_turtle, game_state):
        '''
        Function -- draw_pieces
            draw pieces according to the pieces state
        Parameters:
            a_turtle -- an instance of Turtle
        Returns:
            Nothing. Draws a square in the graphics window.
        '''
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if game_state.squares[row][col] != "EMPTY":
                    if game_state.squares[row][col] == "BLACK":
                        a_turtle.color(self.SQUARE_COLORS[0], self.CIRCLE_COLORS[0])
                    if  game_state.squares[row][col] == "RED":
                        a_turtle.color(self.SQUARE_COLORS[0], self.CIRCLE_COLORS[1])                
                    a_turtle.setposition(
                                        self.start + self.SQUARE * col + self.SQUARE / 2,
                                        self.start + self.SQUARE * row)
                    self.draw_circle(a_turtle, self.SQUARE / 2)


    def  draw_highlight(self, a_turtle, game_state):
        '''
        Function -- draw_highlight
            draw the selected pieces and its legal diagonal
        Parameters:
            a_turtle -- an instance of Turtle
        Returns:
            Nothing. Draws a square in the graphics window.
        '''
        a_turtle.color("red", "light gray")
        for item in game_state.available_move:
            a_turtle.setposition(self.start + item[1] * self.SQUARE, self.start + item[0] * self.SQUARE)
            self.draw_square(a_turtle, self.SQUARE)
        a_turtle.color("blue", "light gray")
        x = game_state.selected_piece[0]
        y = game_state.selected_piece[1]
        a_turtle.setposition(self.start + y * self.SQUARE, self.start + x * self.SQUARE)
        self.draw_square(a_turtle, self.SQUARE)


    def draw_square(self, a_turtle, size):
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


    def draw_circle(self, a_turtle, radius):
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