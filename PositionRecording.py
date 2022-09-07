'''
CS5001
Fall 2021 
Final Project
Othello Game
Carlin Huang
'''

'''
Class: PositionRecording
This class records and returns the position
'''
class PositionRecording:
    nothing = None

    def __init__(self):
        '''
        Constructor -- creates new instances of circle
        Parameters: 
            self -- the current object 
        '''
        self.x = 0
        self.y = 0
        

    @classmethod
    def get_instance(cls):
        if PositionRecording.nothing == None:
            PositionRecording.nothing = PositionRecording()
        return PositionRecording.nothing

def record_position(x, y):
    instance = PositionRecording.get_instance()
    instance.x = x
    instance.y = y
    return instance
    
