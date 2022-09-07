'''
CS5001
Fall 2021 
Final Project
Othello Game
Carlin Huang
'''

from model import Model
from view import View
from controller import Controller
view = View(8)
model = Model(8)
controller = Controller(model, view)
controller.display()

