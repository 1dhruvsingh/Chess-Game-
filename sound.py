import pygame

class Sound:

    def _init_(self, path):
        self.path = path 
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)