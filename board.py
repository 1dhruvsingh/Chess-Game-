from const import *
from square import Squares
from piece import *

class board: 
    
    def __init__(self):
        
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self.create()
        self.add_pieces('white')
        self.add_pieces('black')
        
        
    def move(self, piece, move, testing=False):
        initial = move.initial
        final=move.final
        
        en_pasant_empty = self.squares[final.row][final.col].isempty()
        
        #console board move update 
        self.squares[initial.row][initial.col].piece= None
        self.squares[final.row][final.col].piece= piece
        
        if isinstance(piece, Pawn):
            #en passant capture
            diff=final.col - initial.col 
            if diff !=0 and en_passant_empty:
                #console board move update
                self.squares[initial.row][initial.col + diff].piece= None
                self.squares[final.row][final.col].piece= piece
                if not testing:
                    sound= Sound(
                        os.path.join("assets/sounds/capture.wav"))
                    sound.play()
                    
            #pawn promotion
            else:
                self.check_promotion(piece, final)
                
        #king castling
        if isinstance(piece, King):
            if self.castling(initial, final) and not testing:
                diff= final.col- initial.col
                rook= piece.left_rook if (diff<0) else piece.right_rook
                self.move(rook, rook.moves[-1])
                
        #move 
        piece.moved = True 
        
        #clear valid moves
        piece.clear_moves()
        
        #set last move 
        self.last_move = move
        
    def valid_move(self, piece, move):
        return move in piece.moves                                
                    
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
