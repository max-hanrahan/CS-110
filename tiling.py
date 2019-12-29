"""
 *****************************************************************************
   FILE:        tiling.py

   AUTHOR:      Max Hanrahan

   ASSIGNMENT:  Tiling

   DATE:        10/21/2019

   DESCRIPTION: I am shooting for an A+ because this project fulfills the A 
   requirements and performs an extra feature on line 39.

 *****************************************************************************
"""

import turtle
import random

BOARD_SIZE = 4

CELL_SIZE = 100

BACKGROUND_COLOR = 'white'
GRID_COLOR = 'black'
TRI_COLOR = 'red'
DEAD_COLOR = 'pink'
HOLE_COLOR = 'black'

T = turtle.Turtle()

WIN = turtle.Screen()

# give the screen a comfortable border relative to the board size
SCREEN_SIZE = (BOARD_SIZE + 2) * CELL_SIZE
turtle.setup(SCREEN_SIZE, SCREEN_SIZE)

WIN.title("Max Hanrahan's tiling project")# this is my attempt at an A+
WIN.tracer(0)

def main():
    """ The main function. """

    Board()

    WIN.mainloop()

def fill_square(x, y, color):
    ''' sets the position, draws a square, and fills it with the appropritate 
    color'''
    T.penup()
    # Gets to the top left corner
    T.setposition(-(BOARD_SIZE // 2) * CELL_SIZE, (BOARD_SIZE // 2) * CELL_SIZE)

    T.setheading(0) # East
    T.forward(x * CELL_SIZE)
    T.setheading(270) # South
    T.forward(y * CELL_SIZE)

    T.fillcolor(color)
    T.begin_fill()
    T.pendown()

    for _ in range(4):
        T.fd(CELL_SIZE)
        T.left(90)
    T.end_fill()
    T.penup()

class Triomino():
    '''The triomino class which will draw, move, rotate, and 
    check the positon of the triomino'''
    def __init__(self, board):
        # four possible orientations, 0 being L shape, 1 being a clockwise transformation, etc.
        self._orientation = 0 
        # these track the top left cell in the 2x2 region containing triomio
        self._x = 0
        self._y = 0
        self._draw()
        self._board = board

    def _draw(self):
        '''Daw the square in one of four orientations'''
        if self._orientation == 0:
            # orienting the top square, the bottom right square, and the bottom left square
            fill_square(self._x, self._y, TRI_COLOR)
            fill_square(self._x + 1, self._y + 1, TRI_COLOR)
            fill_square(self._x, self._y + 1, TRI_COLOR)

        elif self._orientation == 1:
            # similarly, for the other orientations
            fill_square(self._x, self._y, TRI_COLOR)
            fill_square(self._x + 1, self._y, TRI_COLOR)
            fill_square(self._x, self._y + 1, TRI_COLOR)

        elif self._orientation == 2:
            fill_square(self._x, self._y, TRI_COLOR)
            fill_square(self._x + 1, self._y, TRI_COLOR)
            fill_square(self._x + 1, self._y + 1, TRI_COLOR)

        elif self._orientation == 3:
            fill_square(self._x + 1, self._y, TRI_COLOR)
            fill_square(self._x + 1, self._y + 1, TRI_COLOR)
            fill_square(self._x, self._y + 1, TRI_COLOR)

    def set_triomino(self):
        '''set the triomino down by modifying the gridtracker with X's'''
        if self.check_triomino():
            if self._orientation == 0:
                self._board.get_gridtracker()[self._x][self._y] = 'X'
                self._board.get_gridtracker()[self._x][self._y + 1] = 'X'
                self._board.get_gridtracker()[self._x + 1][self._y + 1] = 'X'
            elif self._orientation == 1:
                self._board.get_gridtracker()[self._x][self._y] = 'X'
                self._board.get_gridtracker()[self._x][self._y + 1] = 'X'
                self._board.get_gridtracker()[self._x + 1][self._y] = 'X'
            elif self._orientation == 2:
                self._board.get_gridtracker()[self._x][self._y] = 'X'
                self._board.get_gridtracker()[self._x + 1][self._y] = 'X'
                self._board.get_gridtracker()[self._x + 1][self._y + 1] = 'X'
            elif self._orientation == 3:
                self._board.get_gridtracker()[self._x + 1][self._y] = 'X'
                self._board.get_gridtracker()[self._x][self._y + 1] = 'X'
                self._board.get_gridtracker()[self._x + 1][self._y + 1] = 'X'
        self._board.draw_board()

    def move_up(self):
        '''redraw the board, move up if in boundary, and redraw triomino'''
        if self._y > 0:
            self._board.draw_board()
            self._y -= 1
            self._draw()

    def move_down(self):
        '''redraw the board, move down if in boundary, and redraw triomino'''
        if self._y < BOARD_SIZE - 2:
            self._board.draw_board()
            self._y += 1
            self._draw()

    def move_left(self):
        '''similarly, move left if in boundary'''
        if self._x > 0:
            self._board.draw_board()
            self._x -= 1
            self._draw()

    def move_right(self):
        '''similarly, move right if in boundary'''
        if self._x < BOARD_SIZE - 2:
            self._board.draw_board()
            self._x += 1
            self._draw()

    def rotate(self):
        '''increment the orinetation variable up to 3 and redraw the triomino'''
        self._board.draw_board()
        self._orientation = (self._orientation + 1) % 4
        self._draw()

    def check_triomino(self):
        '''if the triomino has position over and X or H in the grid, 
        it will not be placed'''
        if self._orientation == 0:
            if self._board.get_gridtracker()[self._x][self._y] != 'O' or \
            self._board.get_gridtracker()[self._x][self._y + 1] != 'O'or \
            self._board.get_gridtracker()[self._x + 1][self._y + 1] != 'O':
                return False
        if self._orientation == 1:
            if self._board.get_gridtracker()[self._x][self._y] != 'O' or \
            self._board.get_gridtracker()[self._x][self._y + 1] != 'O' or \
            self._board.get_gridtracker()[self._x + 1][self._y] != 'O':
                return False
        if self._orientation == 2:
            if self._board.get_gridtracker()[self._x][self._y] != 'O' or \
            self._board.get_gridtracker()[self._x + 1][self._y] != 'O' or \
            self._board.get_gridtracker()[self._x + 1][self._y + 1] != 'O':
                return False
        if self._orientation == 3:
            if self._board.get_gridtracker()[self._x + 1][self._y] != 'O' or \
            self._board.get_gridtracker()[self._x][self._y + 1] != 'O' or \
            self._board.get_gridtracker()[self._x + 1][self._y + 1] != 'O':
                return False
        return True

class Board:
    '''draw the board, make the triominos, and use the movements defined above'''
    def __init__(self):
        '''initialize a list of triominos and a grid representing the board'''
        self._triomino = 0
        self._gridtracker = []
        # make an appropriate-sized grid and fill it with O for Open access
        for _ in range(BOARD_SIZE):
            self._gridtracker.append(['O'] * BOARD_SIZE)

        # randomly generate an H in this grid, for hole
        rand_number_x = random.randint(0, BOARD_SIZE - 1)
        rand_number_y = random.randint(0, BOARD_SIZE - 1)
        self._gridtracker[rand_number_x][rand_number_y] = 'H'

        self.draw_board()

        # call all the methods with the appropriate input
        WIN.listen()
        WIN.onkey(self.make_triomino, 't')
        WIN.onkey(self.rotate_last_tri, 'r')
        WIN.onkey(self.move_up_last_tri, 'Up')
        WIN.onkey(self.move_down_last_tri, 'Down')
        WIN.onkey(self.move_left_last_tri, 'Left')
        WIN.onkey(self.move_right_last_tri, 'Right')

    def get_gridtracker(self):
        '''a getter for the gridtracker so that it may be mutated'''
        return self._gridtracker

    def draw_board(self):
        '''draws the board square-by-square with color according to the grid'''
        T.color(GRID_COLOR)

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self._gridtracker[row][col] == 'O':
                    color = BACKGROUND_COLOR
                elif self._gridtracker[row][col] == 'H':
                    color = HOLE_COLOR
                else:
                    color = DEAD_COLOR

                fill_square(row, col, color)

    # since passing methods from _triomino to onkey doesn't update, it is 
    # necessary to create the following helper functions: 
    # (suggested by Ben Kallus (TA))
    
    def make_triomino(self):
        '''creates triomino if it's the first one to be made, 
        or makes a new one that is mutable'''
        if self._triomino != 0:
            self._triomino.set_triomino()
        if self.celebrate():
            return
        self._triomino = Triomino(self)

    def rotate_last_tri(self):
        '''rotates'''
        if self._triomino != 0:
            self._triomino.rotate()

    def move_up_last_tri(self):
        '''moves up'''
        if self._triomino != 0:
            self._triomino.move_up()

    def move_down_last_tri(self):
        '''moves down'''
        if self._triomino != 0:
            self._triomino.move_down()

    def move_right_last_tri(self):
        '''moves right'''
        if self._triomino != 0:
            self._triomino.move_right()

    def move_left_last_tri(self):
        '''moves left'''
        if self._triomino != 0:
            self._triomino.move_left()

    def celebrate(self):
        '''once there are no o's left, display a celebratory message only'''
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self._gridtracker[r][c] == 'O':
                    return False

        print('You are the winner!')
        # make all the key commands bind to nothing so the game ends
        WIN.onkey(None, 't')
        WIN.onkey(None, 'r')
        WIN.onkey(None, 'Up')
        WIN.onkey(None, 'Down')
        WIN.onkey(None, 'Left')
        WIN.onkey(None, 'Right')
        T.reset()
        # turtle.write() was shown to me via Ben Kallus (TA)

        turtle.write("You win!", True, align='center', font=('Proxima Nova', 64, 'normal'))
        return True
            
if __name__ == '__main__':
    main()