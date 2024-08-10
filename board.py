from const import *
from square import Squares
from piece import *

class board: 
    
    def __init__(self):
        
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        
        self.create()
        self.add_pieces('white')
        self.add_pieces('black')
        
    def create(self):
        for row in range(ROWS):
            for col in range (COLS):
                self.squares[row][col] = Squares(row,col)
              
    def add_pieces(self, colour):
        if colour =="white":
            row_pawn ,row_other = (6,7)
        else:
            row_pawn ,row_other = (1,0)
           
        #PAWNS 
        for col in range(COLS):
            self.squares[row_pawn][col]= Squares(row_pawn ,col, Pawn(colour))
            
        #KNIGHTS
        self.squares[row_pawn][1]= Squares(row_pawn ,1, Knight(colour))
        self.squares[row_pawn][6]= Squares(row_pawn ,6, Knight(colour))
        
        #BISHOPS
        self.squares[row_pawn][2]= Squares(row_pawn ,2, Bishop(colour))
        self.squares[row_pawn][5]= Squares(row_pawn ,5, Bishop(colour))
        
        #ROOKS
        self.squares[row_pawn][0]= Squares(row_pawn ,0, Rook(colour))
        self.squares[row_pawn][7]= Squares(row_pawn ,7, Rook(colour))
        
        #QUEEN
        self.squares[row_pawn][3]= Squares(row_pawn ,3, Queen(colour))
        
        #KING
        self.squares[row_pawn][4]= Squares(row_pawn ,4, King(colour))
    
            
    
b=board()
b.create()