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
            
            #if clicked 

        
   
main=Main()
main.mainloop()            
        