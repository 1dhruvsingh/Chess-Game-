from const import *
from square import Square

class board: 
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.create()
        
    def create(self):
        for row in range(ROWS):
            for col in range (COLS):
                self.squares[row][col] = Square(row,col)
              
    def add_pieces(self, colour):
        pass
    
b=board()
b.create()