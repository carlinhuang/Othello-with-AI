'''
CS5001
Fall 2021 
Final Project
Othello Game
Carlin Huang
'''

'''
Class: Model 
The model is responsible for managing the data of the application
It responds to the request from the view
It also responds to instructions from the controller to update itself
'''
DIRECTION =[[0, 1], [1, 1], [1, 0], [1, -1],[0, -1], [-1, -1], [-1, 0], [-1, 1]]
FILENAME = "scores.txt"
SQUARE = 50

class Model:
    def __init__(self, n):
        '''
        Constructor -- creates new instances of circle
        Parameters: 
            self -- the current object 
            n -- the number of row and column
        Raises: 
            ValueError when n is not positive or n is not even
            TypeError when n is not integer 
        '''
        if not isinstance(n,int):
            raise TypeError("n must be integer")
        if n<= 0 or n%2 != 0:
            raise ValueError("n must be an even positive number")
        self.n = n
        self.tile_number = 0
        self.chessboard = self.create_chessboard(n)
        self.set_center_tile(n)

    def __str__(self):
        """
        Method -- returns a string that represents view
        Parameters:
           self -- the current object
        """
        output = "This is a text-chessboard with height and width of " + str(self.n)
        return output
        
    def __eq__(self, other):
        """
        Method -- returns a boolean to test if two objects'n are equal
        Parameters:
           self -- the current object
           other -- the other object
        """
        return self.n == other.n
    def create_chessboard(self,n):
        '''
        Method -- creates the chessboard with nested list
        Parameters: 
            self -- the current object 
            n -- the number of row and column
        Returns: a text-based chessboard
        Raises: 
            ValueError when n is not positive or n is not even
            TypeError when n is not integer 
        '''
        if not isinstance(n,int):
            raise TypeError("n must be integer")
        if n<= 0 or n%2 != 0:
            raise ValueError("n must be an even positive number")
        chessboard = []
        for i in range(n):
            chessboard.append([])
            for j in range(n):
                chessboard[i].append("E")
        return chessboard

            
    def get_color(self):
        '''
        Method -- get the color of tile
        Parameters: 
            self -- the current object 
        Returns:
            "B" or "W'
        Raises: 
            TypeError when tile_number is not integer
            ValueError when tile_number is negative
        '''
        if not isinstance(self.tile_number,int):
            raise TypeError("tile_number must be integer")
        if self.tile_number < 0:
            raise ValueError("tile_number must be non-negative number")
        if self.tile_number % 2 == 0:
            return "B"
        else: 
            return "W"
    
        
    def set_color(self):
        '''
        Method -- sets a dictionary to translate "B" to "black", "W" to "white" 
        Parameter: 
            self -- the current object 
        Returns: a dictionary that translates "B" to "black", "W" to "white" 
        '''
        dictionary = {"B": "black", "W": "white"}
        return dictionary[self.get_color()]
    
    def set_center_tile(self,n):
        '''
        Method -- sets the center tiles 
        Parameters: 
            self -- the current object 
            n -- the number of row and column
        Raises: 
            ValueError when n is not positive or n is not even
            TypeError when n is not integer 
        '''
        if not isinstance(n,int):
            raise TypeError("n must be integer")
        if n<= 0 or n%2 != 0:
            raise ValueError("n must be an even positive number")
        self.chessboard[int(n/2-1)][int(n/2-1)] = "W"
        self.chessboard[int(n/2)][int(n/2)] = "W"
        self.chessboard[int(n/2-1)][int(n/2)] = "B"
        self.chessboard[int(n/2)][int(n/2-1)] = "B"


    def is_on_board(self, column, row):
        '''
        Method -- check whether a square is on chessboard
        Parameters: 
            self -- the current object 
            column, row -- the column and row of the tile
        Returns:
            True when a square is on chessboard
            False when a square is not on chessboard
        Raises: 
            TypeError when column or row is not integer 
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        if 0 <= column < self.n and 0 <= row < self.n:
            return True
        else: 
            return False
            
    def is_empty(self,column,row):
        '''
        Method -- check whether a square is empty
        Parameters: 
            self -- the current object 
            column, row -- the column and row of the tile
        Returns:
            True when a square is empty
            False when a square is not empty
        Raises: 
            TypeError when column or row is not integer 
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        if self.chessboard[row][column] != "E":
            return False
        else:
            return True
        
    def is_legal_move(self, column, row):
        '''
        Method -- see whether the move is legal 
        Parameters: 
            self -- the current object 
            column, row -- the column and row of the square
        Returns:
            False when a move is not legal move
            a list of tiles that can be flipped when a move is legal move
        Raises: 
            TypeError when column or row is not integer 
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        if not (self.is_empty(column, row) and self.is_on_board(column, row)):
            return False

        tile = self.get_color()
        if tile == "B":
            other_tile = "W"
        else:
            other_tile = "B"

        tiles_can_be_flipped = []
        for direction in DIRECTION:
            column_direction = direction[0]
            row_direction = direction[1]
            x = int(column) 
            y = int(row)
            x += column_direction
            y += row_direction
            while self.is_on_board(x,y) == True and self.chessboard[int(y)][int(x)] == other_tile:
                x += column_direction
                y += row_direction
                if self.is_on_board(x,y) == True and self.chessboard[int(y)][int(x)] == tile:
                    while True:
                        x -= column_direction
                        y -= row_direction
                        if int(x) == column and int(y) == row:
                            break
                        tiles_can_be_flipped.append([int(x),int(y)])
        #print(len(tiles_can_be_flipped))       
        if len(tiles_can_be_flipped) == 0:
            return False
        return tiles_can_be_flipped
    
    def get_valid_move(self):
        '''
        Method -- get all the valid move for player
        Parameters: 
            self -- the current object 
        Returns:
            a list of position that the player can play tiles at
        '''
        valid_move = []
        for column in range(0, self.n):
            for row in range(0, self.n):
                if self.is_legal_move(column,row):
                    valid_move.append([column,row])
        return valid_move
                
    def get_flipped(self,lst,player):
        '''
        Method -- see whether the move is legal 
        Parameters: 
            self -- the current object 
            lst -- a list
            player -- the color of player
        Raises: 
            TypeError when lst is not a list
            ValueError when player is not B or W
        '''
        if not isinstance(lst,list):
            raise TypeError("lst must be a list")
        if player != "W" and player!= "B":
            raise ValueError("player must be B or W")
        for tile in lst:
            column = tile[0]
            row = tile[1]
            if self.chessboard[row][column] != player:
                self.chessboard[row][column] = player

        
    def move(self,column,row):
        '''
        Method -- if the move is a legal move, make the move on text-based chessboard
        Parameters:
            self -- the current object
            column, row -- the column and row of the square
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise ValueError("row and column must be an integer")
        tiles_can_be_flipped = self.is_legal_move(column,row)
        if tiles_can_be_flipped:
            player = self.get_color()
            self.chessboard[int(row)][int(column)]= player
            self.get_flipped(tiles_can_be_flipped,player)
            self.tile_number += 1
            
    def is_game_over(self, lst):
        '''
        Method -- see whether the game is over 
        Parameters:
            self -- the current object
        Returns:
            True if the game is over
            False if the game is not over
        Raises: TypeError when lst is not a list
        '''
        if not isinstance(lst,list):
            raise TypeError("lst must be a list")
        
        if len(lst) == 0:
            return True
        else:
            return False


    def count_B_and_W(self):
        '''
        Method -- count the number of black and white tiles
        Parameters:
            self -- the current object
        Returns: the number of black and white tiles on text-based chessboard 
        '''
        black = 0
        white = 0
        for lines in self.chessboard:
            black += lines.count("B")
            white += lines.count("W")
        return black, white
    
    def get_winner(self,black_score,white_score):
        '''
        Method -- compares the scores of black and white, and gets the winner of the game
        Parameters:
            self -- the current object 
            black_score: the number of black tiles 
            white_score: the number of white tiles 
        Returns: a string that annouces winner and score
        Raises: 
            TypeError when black_score or white_score is not integer
            ValueError when black_score or white_score is negative
        '''
        if not (isinstance(black_score, int) and isinstance(white_score, int)):
            raise TypeError("Scores must be integer")
        if black_score<0 or white_score<0:
            raise ValueError("Scores must be non-negative numbers")
        
        if black_score == white_score:
            output = "GAME OVER!! IT’S A TIE!! There are "+str(black_score)+ " of each!"
        elif white_score < black_score:
           output = "GAME OVER!! You win! There are "+str(black_score)+" black tiles!"   
        else:
            output = "GAME OVER!! Computer wins! There are "+str(white_score)+" white tiles!"   
        return output 

            
    def print_information(self):
        '''
        Method -- prints information
        Parameters:
            self -- the current object
        '''
        
        #print(self.count_B_and_W())
        print(self.set_color(), "'s turn")
        #print(self.get_valid_move()," is valid for", self.get_color())
        #self.print_chessboard()

    
    def get_column_and_row(self, x, y):
        '''
        Method -- gets the column and row of a click
        Parameters:
            self -- the current object  
            x, y -- the position of click in turtle
            if x or y are out of range, nothing will happen
        Returns: column and row of the click
        '''
        if -(self.n/2*50)<x<self.n/2*50 and -(self.n/2*50)<y<self.n/2*50: 
            column = int((x + (self.n/2) * SQUARE) // SQUARE)
            row = int((-y + (self.n/2) * SQUARE) // SQUARE)
        return column, row

    def get_the_dot_position_of_circle(self,column, row):
        '''
        Method -- get the dot position of the circle so that the circle is drawed in the center of the square
        Parameters:
            self -- the current object
            column, row -- the column and row of the clicked square
        Raises:
            TypeError when column or row is not integer
        Returns: x-axis and y-axis of the drawing dot
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        x = column * SQUARE - (self.n-1)/2 * SQUARE
        y = (self.n-1)/2 * SQUARE - row * SQUARE
        return x, y

    
    def get_column_and_row(self, x, y):
        '''
        Method -- gets the column and row of a click
        Parameters:
            self -- the current object  
            x, y -- the position of click in turtle
            if x or y are out of range, nothing will happen
        Returns: column and row of the click
        '''
        if -(self.n/2*50)<x<self.n/2*50 and -(self.n/2*50)<y<self.n/2*50: 
            column = int((x + (self.n/2) * SQUARE) // SQUARE)
            row = int((-y + (self.n/2) * SQUARE) // SQUARE)
        return column, row

    def get_the_dot_position_of_circle(self,column, row):
        '''
        Method -- get the dot position of the circle so that the circle is drawed in the center of the square
        Parameters:
            self -- the current object
            column, row -- the column and row of the clicked square
        Raises:
            TypeError when column or row is not integer
        Returns: x-axis and y-axis of the drawing dot
        '''
        if not (isinstance(column, int) and isinstance(row, int)):
            raise TypeError("row and column must be an integer")
        x = column * SQUARE - (self.n-1)/2 * SQUARE
        y = (self.n-1)/2 * SQUARE - row * SQUARE
        return x, y
    def score_file(self,score):
        '''
        Method -- write the name and score into file, if file does not exist, create a new file
        Parameters:
            self -- the current object 
            score: the score of a game
        Raises: 
            TypeError when score is not integer
            ValueError when score is negative
        '''
        if not isinstance(score, int):
            raise TypeError("Scores must be integer")
        if score<0:
            raise ValueError("Scores must be non-negative numbers")
        
        user_name = input("Please enter your name\n")
        try: 
            scores = []
            file_content = []   
            file = open(FILENAME,"r")
             
            for lines in file:
                content = lines.strip().split(" ")
                scores.append(int(content[1]))
                file_content.append(content)

                 
            if score < max(scores):
                file_content.append([user_name, str(score)])
            else:
                file_content.insert(0, [user_name, str(score)])
            file.close()

            open(FILENAME, "w").close()

            file = open (FILENAME, "w")
            for i in range(0, len(file_content)):
                file.write(str(file_content[i][0])+" "+str(file_content[i][1])+ "\n")
            file.close()

        except FileNotFoundError:
            with open(FILENAME,"w") as file:
                file.write(user_name+" "+str(score)+ "\n")
        except PermissionError :
            print("You do not have permission to use that file")        
        except OSError:
            print("Something happened while reading or writing the file:", FILENAME)

    
    def get_most_flip_step(self,lst):
        '''
        Method -- get the step with the largest number of flippable opponent tiles
        Parameters:
            self -- the current object 
            lst: a list of valid move
        Returns: the column of row of the optimal move
        Raises: 
            TypeError when lst is not list
        '''
        if not isinstance(lst,list):
            raise TypeError("lst must be a list")
        flip_lst = []
        for moves in lst:
            flip_number = len(self.is_legal_move(moves[0],moves[1]))
            flip_lst.append(flip_number)
        
        max_value = max(flip_lst)
        max_index = flip_lst.index(max_value)
        return lst[max_index][0], lst[max_index][1]

            
    def computer_strategy(self,lst):
        '''
        Method -- generates the best move for computer player
        Parameters:
            self -- the current object
            lst -- a list of valid move
        Returns: the column and row of the optimal move
        '''
        if not isinstance(lst,list):
            raise TypeError("lst must be a list")
        preferred_move = [[0,0],[0,int(self.n)-1],[int(self.n)-1,0],[int(self.n)-1,int(self.n)-1]]
       
        dangerous_move = [[1,1],[1,int(self.n)-2],[int(self.n)-2,1],[int(self.n)-2,int(self.n)-2]]
        for move in preferred_move:
            if move in lst:
                column,row = move[0], move[1]
                return (column, row)
        for move in dangerous_move:
            if move in lst and len(lst)>1:
                lst.remove(move)
                column, row = self.get_most_flip_step(lst)
                return (column,row)
        column, row = self.get_most_flip_step(lst)
        return (column,row)       


        
        
        
            


       
        
        

              
