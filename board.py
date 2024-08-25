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
        
    def valid_move(self,piece, move):
        return move in piece.moves
    
    def  check_promotion(self, piece, final):
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.col].piece = Queen(piece.color)
            
    def castling(self, initial ,final):
        return abs (initial.col - final.col)==2
        
    def set_true_en_passant(self,piece):
        
        if not isinstance(piece,Pawn):
            return 
        for row in range(ROWS):
            for col in range(COLS):
                if isinstance (self.squares[row][col].piece,Pawn):
                    self.squares[row][col].piece.en_passant = False
                    
    def in_check(self, piece , move):
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_piece,move,testing=True)
        
        for row in range(ROW):
            for col in range(COLS):
                if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p = temp_board.squares[row][col].piece
                    temp_board.calc_moves(p, row,col , bool=False)
                    for m in p.moves:
                        if isinstance(m.final.piece, King):
                            return True
                        
    def calc_moves(self,piece,row,col , bool=True ):

        # (calculate all the possible valid moves of an specific position )
        def pawn_moves():
            #steps
            steps=1 if piece.moved else 2

            #vertical moves
            start = row + piece.dir
            end = row + (piece.dir * ( 1 + steps))
            for possible_move_row in range (start ,end ,piece.dir):
                if Squares.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        #create initial and final move squares 
                        initial = Square(row, col)
                        final = Square(possible_move_row,col)
                        #create a new move
                        move = Move(initial, final)

                        #check potential checks 
                        if bool :
                            if not self.in_check(piece,move):
                                #append new move
                                piece.add_move(move)
                        else:
                            #append new move 
                            piece.add_move(move)

                    #blocked 
                    else: break
                #not in range
                else: break 
            
            #diagonal moves 
            possible_move_row = row + piece.dir 
            possible_move_col = [col-1 , col+1]
            for possible_move_col in possible_move_cols:
                if Squares.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        #create initial and final move squares
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row, possible_move_col].piece
                        final = Square(posssible_move_row,possible_move_col, final_piece)
                        move= Move(initial, final)
                        
                        #check potential checks
                        if bool:
                            if not self.in_check(piece ,move):
                                #append new move
                                piece.add_move(move)
                        else:
                            #append new move
                            piece.add_move(move)
                            
            # en passant move
            r = 3 if piece.color == 'white' else 4
            fr = 2 if piece.color == 'white' else 5
            #left en passant 
            if Square.in_range(col-1) and row == r:
                if self.squares[row][col-1].has_enenmy_pieve(piece.color):
                    p = self.squares[row][col-1].piece
                    if isinstance(p,Pawn):
                        if p.en_passant:
                            #create initial and final move squares
                            initial = Square(row, col)
                            final = Square(fr, col-1, p)
                            #create a new move 
                            move = Move(initial ,final)
                            
                            #check potential checks 
                            if bool:
                                if not self.in_check(piece, move):
                                    #append new move 
                                    piece.add_move(move)
                                else:
                                    #append new move 
                                    piece.add_move(move)

            #right en passant
            if Square.in_range(col+1) and row == r:
                if self.squares[row][col+1].has_enemy_piece(piece.color):
                    p = self.squares[row][col+1].piece
                    if isinstance(p,Pawn):
                        if p.en_passant:
                            #create initial and final  move squares
                            initial = Square(row,col)
                            final = Square(fr, col+1, p)
                            #create a new move
                            move = Move(initial ,final)
                            
                            #check potential checks 
                            if bool:
                                if not self.in_check(piece, move):
                                    #append new move
                                    piece.add_move(move)
                            else:
                                 #append new move
                                 piece.add_move(move)
    
        def knight_moves():
             # 8 possible moves
             possible_moves = [
             (row-2, col+1),
             (row-1, col+2),
             (row+1, col+2),
             (row+2, col+1),
             (row+2, col-1),
             (row+1, col-2),
             (row-1, col-2),
             (row-2, col-1),
             ] 
          for possible_move in possible_moves:
            possible_move_row, possible_move_col = possible_moves
            
            if Squares.in_range(possible_move_row, possible_move_col):
                if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                    #create squares of the new move 
                    initial = Square(row,col)
                    final_piece = self.squares[possible_move_row, possible_move_col, final_piece].piece
                    final= Square(possible_move_row, possible_move_col, final_piece)
                    #crete new move
                    move = Move(initial ,final)
                    
                    #check potential checks 
                    if bool:
                        if not self.in_check(piece, move):
                            #append new move
                            piece.add_move(move)
                        else:
                          break
                    else:
                        #append new move 
                        piece.add_move(move)
                                        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incrs, col_incr= incr
                possible_move_row =  row + row_incr
                possible_move_col =  col + col_incr 

                while True:
                    if Square.in_range(possible_move_row, possible_move_col ):
                        #create squares of the possible new move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row, possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_move)
                        #create a possible new move
                        movce= Move(initial ,final)

                        #empty = contine looping
                        if self.squares[possible_move_row,possible_move_col].isempty():
                            #check potential checks 
                            if bool:
                                if not self.in_check(piece ,move):
                                #append new move 
                                piece.add_move(move)
                            else:
                                #append new move
                                piece.add_move(move)
                        
                        #has enemy piece = add move + break
                        elif self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            #check potential checks 
                            if bool:
                                if not self.incheck(piece ,move):
                                    #append new move
                                    piece.add_move(move)
                            else:
                                #append new move
                                piece.add_move(move)
                            break
                        
                        # has team piece = break 
                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    #not in range
                    else:
                        break

                    #incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            adjs = [
                (row-1, col+0), #up
                (row-1, col+1), #up-right 
                (row+0, col+1), #right 
                (row+1, col+1), #down-right
                (row+1, col-1), #down
                (row+1, col-1), #down-left
                (row+0, col-1), #left
                (row-1, col-1), #up-left
            ]
            
            # normal moves 
            for possible_move in adjs:
                possible_more_rows ,possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        #create squares of the new move 
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) #piece = piece
                        #create new move
                        move= Move(initial ,final)
                        #create potential checks 
                        if bool:
                            if not self.in_check(piece, move):
                                #append new move
                                piece.add_move(move)
                            else: 
                                break
                        else:
                            #append new move
                            piece.add_move(move)

            #castling moves
            if not piece.moved:
                #queen castling
                left_rook = self.squares[row][0].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1,4):
                            #castling is not possible because there are pieces in b/w ?
                            if self.squares[row][c].has_piece():
                                break

                            if c == 3:
                                #adds left rook to king 
                                piece.left_rook = left_rook

                                #rook move
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                Move_R= Move(initial ,final)

                                #king move
                                initial =Square(row,col)
                                final = Square(row, 2)
                                Move_K = Move(initial, final)

                                #check for potential checks
                                if bool:
                                    if not self.in_check(piece, Move_K) and not self.in_check(left_rook, Move_R):
                                        #apend new move to the rook
                                        left_rook.add_move(Move_R)
                                        #append new move to the king
                                        piece.add_move(Move_K)
                                    else:
                                        #append new to move to the rook
                                        left_rook.add_move(Move_R)
                                        #append new move to the king
                                        piece.add_move(Move_K)
                                       
                                    

   #START HERE *********************************************************************

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
