import pygame
from const import *
from board import board

class  Game:
    
    def __init__(self):
        self.baord = Board()
    
    #show methods
    
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col ) % 2== 0:
                    colour = (234,235,200) #light green
                else:
                    colour= (119,154,88) #dark green
                    
                rect = (col * SQSIZE,row * SQSIZE , SQSIZE ,SQSIZE)
                pygame.draw.rect(surface,colour,rect)
                
    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                #piece?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].has_piece
                    img= pygame.image.load(piece.texture)
                    img_center = col* SQSIZE + SQSIZE //2 , row* SQSIZE +SQSIZE//2
                    piece.texture_rect=img.et_rect(center= img_center)
                    surface.blit(img ,piece.texture_rect)
            