'''
CS5001
Fall 2021
Othello Game Milestone2
Carlin Huang
'''

from model import Model
from view import View
from view import SQUARE

'''
Class: Controller 
This is the controller of MVC framework.
It responsible for controlling the flow of the application execution. 
It calls the methods in other class to achieve the goals.
'''
class Controller:
    def __init__(self,model,view):
        ''' 
        Constructor -- creates new instances of Controller
        Parameters:
            self -- the current object
            model -- the model
            view -- the view
        '''
        self.view = view
        self.model = model
        self.n = self.view.n

    def __str__(self):
        """
        Method -- returns a string that represents view
        Parameters:
           self -- the current object
        """
        output = "This is a controller of the Othello game"
        return output
        
    def __eq__(self, other):
        """
        Method -- returns a boolean to test if two objects are equal
        Parameters:
           self -- the current object
           other -- the other object
        """
        return self.view == other.view and self.model == other.model  

    def display(self):
        '''
        Method -- displays the results of model in view
        Parameter:
            self -- the current object
        '''
        self.view.draw_board(self.view.n)
        self.view.draw_center_tile()
        print("black's turn")
        self.view.screen_click(self.draw_circles_in_view)


    def flipping(self,column,row,color):
        '''
        Method -- flip the opponent file
        Parameters:
            self -- the current object
            column, row -- the column and row of the clicked square
            color -- the color of tile
        Raises:
            TypeError when column or row is not integer
            TypeError when color is not string
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be integer")
        if not isinstance(color, str):
            raise TypeError("color must be string")
        tiles_can_be_flipped = self.model.is_legal_move(column,row)
        if tiles_can_be_flipped:
            new_x, new_y = self.model.get_the_dot_position_of_circle(column, row)
            self.view.draw_circle(new_x, new_y, color)
            
            for tile in tiles_can_be_flipped:
                column_new = tile[0]
                row_new = tile[1]
                n_x, n_y = self.model.get_the_dot_position_of_circle(column_new, row_new)
                self.view.draw_circle(n_x, n_y, color)
                

    def overall_operation(self, column, row, color):
        '''
        Method -- overall operations for each move: flip opponent tile, move the text-based tile \
            accordingly in model, print information
        Parameters:
            self -- the current object
            column, row -- the column and row of the square
            color -- the color of tile
        Raises:
            TypeError when column or row is not integer
            TypeError when color is not string
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        
        self.flipping(column,row,color)
        self.model.move(column, row)
        self.model.print_information()

        
    def operations_after_game_over(self, black_score, white_score):
        '''
        Method -- operations after games over, including annoucing winner and scoring file
        Parameters:
            self -- the current object
            black_score: the number of black tiles 
            white_wile: the number of white tiles 
        Raises:
            TypeError when black_score or white_score is not integer
            ValueError when black_score or white_score is negative
        '''
        if not (isinstance(black_score, int) and isinstance(white_score, int)):
            raise TypeError("Scores must be integer")
        if black_score<0 or white_score<0:
            raise ValueError("Scores must be non-negative numbers")
        output = self.model.get_winner(black_score, white_score)
        print(output)
        self.model.score_file(black_score)
                
    def draw_circles_in_view(self,x,y):
        '''
        Method -- draws all the circles in view
        Parameters:
            self -- the current object  
            x, y -- the position of click in turtle
        If x or y is out of range, nothing will happen
        '''
        if -(self.n/2*50)<x<self.n/2*50 and -(self.n/2*50)<y<self.n/2*50:
            valid_move = self.model.get_valid_move()
            black_score, white_score = self.model.count_B_and_W()
            if self.model.is_game_over(valid_move) == False:


                color = self.model.set_color()
                if color == "black":
                    self.view.get_click(x,y)
                    x,y = self.view.return_axis()
                    column, row = self.model.get_column_and_row(x, y)
                    self.overall_operation(column,row,color)


                color = self.model.set_color()
                if color == "white":
                    valid_move = self.model.get_valid_move()
                    if not valid_move:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                        self.operations_after_game_over(black_score, white_score)
                        return

                    column, row = self.model.computer_strategy(valid_move)
                    self.overall_operation(column,row,color)

                color = self.model.set_color()
                valid_move = self.model.get_valid_move()
                if not valid_move:
                    self.operations_after_game_over(black_score, white_score)

                
            
        
            
            
            
     
        



        
    
