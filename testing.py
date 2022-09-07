'''
CS5001
Fall 2021 
Final Project
Othello Game
Carlin Huang
'''
import unittest
from model import Model
import os

model1 = Model(2)
model2 = Model(4)
model3 = Model(8)

class testModel(unittest.TestCase):
    '''
    testing methods in class Model
    '''
    def test_init_basic(self):
        self.assertEqual(model2.n, 4)
        self.assertEqual(model2.tile_number, 0)
        
    def test_init_raise_error(self):
        with self.assertRaises(ValueError):
            model0 = Model(0)
            
    def test_str(self):
        self.assertEqual(str(model2),"This is a text-chessboard with height and width of 4") 

    def test_create_chessboard_with_n_equals_zero_raise_ValueError(self):
        with self.assertRaises(ValueError):
            model1.create_chessboard(0)
            model1.create_chessboard(1)
    def test_create_chessboard_with_n_is_not_integer(self):
        with self.assertRaises(TypeError):
            model1.create_chessboard(1.5)
            
    def test_create_chessboard_with_n_equals_two(self):
        self.assertEqual(model1.chessboard, [['W', 'B'], ['B', 'W']])
        
    def test_create_chessboard_with_n_equals_four(self):
        self.assertEqual(model2.chessboard, [['E','E','E','E'],['E','W','B','E'], \
                                             ['E','B','W','E'],['E','E','E','E']])
        
    def test_get_color_raise_ValueError_negative(self):
        with self.assertRaises(ValueError):
            model3.tile_number = -1
            model3.get_color()

    def test_get_color_raise_Typeerror_float(self):
        with self.assertRaises(TypeError):
            model3.tile_number = 1.3
            model3.get_color()
            
    def test_get_color_W(self):
        model3.tile_number = 3
        self.assertEqual(model3.get_color(),"W")
        
    def test_get_color_B(self):
        model3.tile_number = 10
        self.assertEqual(model3.get_color(),"B")
        
    def test_set_color_black(self):
        model3.tile_number = 10
        self.assertEqual(model3.set_color(),"black")
        
    def test_set_color_white(self):
        model3.tile_number = 3
        self.assertEqual(model3.set_color(),"white")
   
    def test_set_center_tile_with_n_is_float_raise_ValueError(self):
        with self.assertRaises(TypeError):
            model1.set_center_tile(1.5)
            
    def test_set_center_tile_with_n_is_odd_number_raise_ValueError(self):
        with self.assertRaises(ValueError):
            model1.set_center_tile(3)
    
    def test_set_center_tile_with_n_equals_four(self):
        model2.set_center_tile(4)
        self.assertEqual(model2.chessboard[1][1], "W")
        self.assertEqual(model2.chessboard[1][2], "B")
        
    def test_is_on_board_raise_Typeerror(self):
        with self.assertRaises(TypeError):
            model1.is_on_board(0.5,1)
            model1.is_on_board(1,"1")
        
    def test_is_on_board(self):
        self.assertTrue(model3.is_on_board(6,7))

    def test_is_on_board_negative_number(self):
        self.assertFalse(model3.is_on_board(-1, 1))
    
    def test_is_on_board_out_of_board(self):
        self.assertFalse(model3.is_on_board(9, 1))

    def test_is_empty_raise_error(self):
        with self.assertRaises(TypeError):
            model2.is_empty(0.5,1)
            model2.is_empty("a",1)
            
    def test_is_empty(self):
        self.assertTrue(model3.is_empty(1,1))
        
    def test_is_empty_False(self):
        self.assertFalse(model3.is_empty(4,4))
        
    def test_is_legal_move_raise_error(self):
        with self.assertRaises(TypeError):
            model2.is_legal_move(1,1.5)
            
    def test_is_legal_move_case1(self):
        model3.tile_number = 0
        self.assertEqual(model3.is_legal_move(3,2),[[3,3]])
        
    def test_is_legal_move_case2(self):
        model3.tile_number = 0
        self.assertEqual(model3.is_legal_move(4,5),[[4,4]])
        
    def test_is_legal_move_False(self):
        model3.tile_number = 1
        self.assertFalse(model3.is_legal_move(6,1))
        
    def test_get_valid_move(self):
        model3.tile_number = 0
        self.assertEqual(model3.get_valid_move(),[[2, 3], [3, 2], [4, 5], [5, 4]])
        
    def test_get_valid_move_False(self):
        model3.tile_number = 1
        self.assertNotEqual(model3.get_valid_move(),[[2, 3], [3, 2], [4, 5], [5, 4]])

    def test_get_flipped_raise_TypeError(self):
        with self.assertRaises(TypeError):
            model2.get_flipped(1,"W")
            
    def test_get_flipped_raise_ValueError(self):
        with self.assertRaises(ValueError):
            model2.get_flipped([[1,3]],"white")    
    
    def test_get_flipped_case1(self):
        model4 = Model(8)
        model4.get_flipped([[4,4]],"B")
        self.assertEqual(model4.chessboard[4][4], "B")

    def test_get_flipped_case2(self):
        model4 = Model(8)
        model4.get_flipped([[4,4]],"W")
        self.assertEqual(model4.chessboard[4][4], "W")
        
    def test_move_raise_error(self):
        with self.assertRaises(ValueError):
            model2.move(0.5,1)
               
    def test_move_success(self):
        model5 = Model(8)
        column = 5
        row = 4
        model5.move(column,row)
        self.assertEqual(model5.tile_number, 1)
        
    def test_move_falied(self):
        model6 = Model(8)
        column = 7
        row = 4
        model6.move(column,row)
        self.assertNotEqual(model6.tile_number, 1)
        
    def test_is_game_over_raise_error(self):
        with self.assertRaises(TypeError):
            model2.is_game_over(1)
            
    def test_is_game_over_yes(self):
        lst = []
        self.assertTrue(model2.is_game_over(lst))

    def test_is_game_over_no(self):
        lst = [[2,3]]
        self.assertFalse(model3.is_game_over(lst))

    def test_count_B_and_W(self):
        model7 = Model(4)
        model7.chessboard = [['E','E','E','E'],['E','W','B','E'],['E','B','W','E'],['E','E','E','E']]
        self.assertEqual(model7.count_B_and_W(),(2,2))

    def test_get_winner_raise_TypeError(self):
        with self.assertRaises(TypeError):
            model2.get_winner(3.5, 3)
        with self.assertRaises(TypeError):
            model2.get_winner(3, "3")
            
    def test_get_winner_raise_ValueError(self):
        with self.assertRaises(ValueError):
            model2.get_winner(-1, 3)
        with self.assertRaises(ValueError):
            model2.get_winner(1, -1)
            
    def test_get_winner(self):
        self.assertEqual(model2.get_winner(8,8),"GAME OVER!! IT’S A TIE!! There are 8 of each!")
        self.assertEqual(model2.get_winner(7,8),"GAME OVER!! Computer wins! There are 8 white tiles!")
        self.assertEqual(model2.get_winner(9,5),"GAME OVER!! You win! There are 9 black tiles!")

    def test_get_column_and_row(self):
        self.assertEqual(model2.get_column_and_row(-75,75),(0,0))
        self.assertEqual(model2.get_column_and_row(75,-75), (3,3))
        self.assertEqual(model3.get_column_and_row(175,-175), (7,7))
        
    def test_get_the_dot_position_of_circle_raise_error(self):
        with self.assertRaises(TypeError):
            model2.get_the_dot_position_of_circle(1.5,1)
            
    def test_get_the_dot_position_of_circle(self):
        self.assertEqual(model2.get_the_dot_position_of_circle(1,1), (-25,25))
        self.assertEqual(model2.get_the_dot_position_of_circle(0,0), (-75,75))
        self.assertEqual(model3.get_the_dot_position_of_circle(0,0), (-175,175))
        
    def test_score_file_raise_TypeError(self):
        with self.assertRaises(TypeError):
            model2.score_file(1.5)
            
    def test_score_file_raise_ValueError(self):
        with self.assertRaises(ValueError):
            model2.score_file(-1)
            
    def test_get_most_flip_step_raise_TypeError(self):
        with self.assertRaises(TypeError):
            model2.get_most_flip_step(1.5)
            
    def test_get_most_flip_step_case1(self):
        model8 = Model(4)
        model8.move(2,3)
        model8.move(1,3)
        model8.move(0,1)
        self.assertEqual(model8.get_most_flip_step([[1, 0], [3, 1], [3, 3]]),(1,0))
        
    def test_get_most_flip_step_case2(self):
        model9 = Model(4)
        model9.move(2,3)
        model9.move(1,3)
        model9.move(0,2)
        self.assertEqual(model9.get_most_flip_step([[3,1], [3,3]]),(3,1))

    def test_get_most_flip_step_case3(self):
        model10 = Model(4)
        model10.move(2,3)
        model10.move(1,3)
        model10.move(0,2)
        model10.move(3,1)
        model10.move(3,2)
        self.assertEqual(model10.get_most_flip_step([[0,3], [3,3]]),(3,3))
        
    def test_computer_strategy_occupy_corner_case1(self):
        model11 = Model(4)
        model11.move(1,0)
        self.assertEqual(model11.computer_strategy([[0, 0], [0, 2], [2, 0]]),(0,0))
        
    def test_computer_strategy_occupy_cornercase2(self):
        model12 = Model(4)
        model12.move(3,2)
        self.assertEqual(model12.computer_strategy([[1, 3], [3, 1], [3, 3]]),(3,3))

    def test_computer_strategy_avoid_dangerous_move(self):
        model13= Model(6)
        model13.move(3,4)
        model13.move(2,4)
        model13.move(1,2)
        self.assertNotEqual(model13.computer_strategy([[2, 1], [4, 2], [4, 4]]), (4,4))
         
        
def main():
    unittest.main(verbosity=3)



if __name__ == '__main__':
    main()
