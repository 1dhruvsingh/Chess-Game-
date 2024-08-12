import pygame
import sys

from const import *
from game import Game
from square import Squares
from move import Move

class Main:
    
    def __init(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game =Game()
        
    def mainloop(self):
        
        screen =self.screen
        game =self.game
        board=self.game.board
        dragger=self.game.dragger
     
      while True:
            
         #show methods
         game.show_bg(screen)
         game.show_last_move(screen)
         game.show_moves(screen)
         game.show_pieces(screen)
         game.show_hover(screen)
         
    
             if dragger.dragging:
                dragger.update_blit(screen)
        
             for event in pygame.event.get():
        
                #click
                  if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
            
                    clicked_row= dragger.mouseY//SQSIZE
                    clicked_col= dragger.mousex//SQSIZE
            
                   #if clicked square has a piece ?
                   if board.squares[clicked_row][clicked_col].has_piece():
                      piece=board.squares[clicked_row][clicked_col].piece
                      #valid piece(color) ?
                      if piece.color==game.next_player:
                          board.calc_moves(piece,clicked_row,clicked_col,bool=True)
                          dragger.save_initial(event.pos)
                          dragger.drag_piece(piece)
                          #show methods
                          game.show_bg(screen)
                          game.show_last_move(screen)
                          game.show_moves(screen)
                          game.show_pieces(screen)
                 
                   #mouse motion
                   elif event.type==gygame.MOUSEMOTION:
                       motion_row=event.pos[1]//SQSIZE
                       motion_col=event.pos[0]//SQSIZE
              
                       game.set_hover(motion_row,motion_col)
              
                       if dragger.dragging:
                           dragger.update_mouse(event.pos)
                           #show methods
                           game.show_bg(screen)
                           game.show_last_move(screen)
                           game.show_moves(screen)
                           game.show_pieces(screen)
                           game.show_hover(screen)
                           dragger.update_blit(screen)
                           
                   #click release
                   elif event.type==pygame.MOUSEBUTTONUP:
                     
                       #if piece is being dragged
                       if dragger.dragging:
                         dragger.update_mouse(event.pos)
                
                
                
            

        
   
main=Main()
main.mainloop()            
        