'''
CS5001
Fall 2021 
Final Project
Othello Game
Carlin Huang
'''

SQUARE = 50
DIAMETER = 40
HALF_SQUARE = 25
from PositionRecording import PositionRecording, record_position
import turtle

'''
Class: View.
It is responsible for all the operations that relates to turtle.
It draws lines, the start chessboard, center tiles, circles with black or white\
    color, and gets the x axis and y axis of click.
'''
class View:
    def __init__(self,n):
        '''
        Constructor -- creates new instances of View
        Parameters:
           self -- the current object
           n -- the number of squares in column and row
        '''
        self.n = n
        self.instance = PositionRecording()
        
    def __str__(self):
        """
        Method -- returns a string that represents view
        Parameters:
           self -- the current object
        """
        output = "This is a chessboard with height and width of " + str(self.n)
        return output

    def __eq__(self, other):
        """
        Method -- returns a boolean to test if two objects'n are equal
        Parameters:
           self -- the current object
           other -- the other object
        """
        return self.n == other.n

    def draw_board(self,n):
        ''' 
        Method -- draws the start chessboard
        Parameters:
           self -- the current object
           n -- the number of squares in column and row
        '''
        self.turt = turtle.Turtle()
        self.turt.hideturtle()
        turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
        turtle.screensize(n * SQUARE, n * SQUARE)
        turtle.bgcolor('white')

     
        # Create the turtle to draw the board
        self.othello = turtle.Turtle()
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()

     
        # Line color is black, fill color is green
        self.othello.color("black", "forest green")

        # Move the turtle to the upper left corner
        corner = -n * SQUARE / 2
        self.othello.setposition(corner, corner)

        # Draw the green background
        self.othello.begin_fill()
        for i in range(4):
            self.othello.pendown()
            self.othello.forward(SQUARE * n)
            self.othello.left(90)
        self.othello.end_fill()
     
        # Draw the horizontal lines
        for i in range(n + 1):
            self.othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines(self.othello, n)

        # Draw the vertical lines
        self.othello.left(90)
        for i in range(n + 1):
            self.othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines(self.othello, n)
            
    def draw_center_tile(self):
        '''
        Method -- draws the four tiles in the center 
        Parameters: 
            self: the current object
        '''
        self.draw_circle(-HALF_SQUARE, HALF_SQUARE,"white")
        self.draw_circle(HALF_SQUARE, -HALF_SQUARE,"white")
        self.draw_circle(HALF_SQUARE, HALF_SQUARE,"black")
        self.draw_circle(-HALF_SQUARE, -HALF_SQUARE,"black")
        
        

    def draw_lines(self,turt,n):
        ''' 
        Method -- draws the line of board
        Parameters:
           self -- the current object
           turt: the turtle
           n -- the number of squares in column and row
        Returns nothing
        '''
        turt.pendown()
        turt.forward(SQUARE * n)
        turt.penup()
        
    def draw_circle(self, x, y, color):
        ''' 
        Method -- draws the line of board
        Parameters:
           self -- the current object
           x, y -- the start position of the circle
           color -- the color of the circle, black or white
        Returns nothing
        '''
        
        self.turt.penup()
        self.turt.setposition(x, y)
        self.turt.pendown()
        
        self.turt.dot(DIAMETER,color)
        #color = self.model.set_color()

        
        
        
    def get_click(self, x, y):
        ''' 
        Method -- records the position of click into instance
        Parameters: 
           self -- the current object
           x, y -- the start position of the circle
        '''
        self.instance = record_position(x, y)
        #self.draw_circle(x, y, color)
        

        
    def screen_click(self, get_click):
        ''' 
        Method -- gets the screen click
        Parameters:
           self -- the current object
           get_click -- a method
        '''
        screen = turtle.Screen()
        screen.onclick(get_click)
        

    def return_axis(self):
        ''' 
        Method -- returns the x axis and y axis of the click
        Parameters:
           self -- the current object
        '''
        return self.instance.x, self.instance.y
    
        
