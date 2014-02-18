import pygame
from GameObject import GameObject
from random import randrange

class PipesController():
    def __init__(self):
        self.pipes = []
    
    def clear(self):
        del self.pipes[:]
    
    def new(self):
        pipepic = pygame.image.load('pipe.png').convert_alpha()
        pipe = GameObject(pipepic, 240, randrange(0, 240), -5, 0)
        self.pipes.append(pipe)

    def draw(self):
        screen = pygame.display.get_surface()
        for pipe in self.pipes:
            screen.blit(pipe.img, pipe.pos)
            pipe.fly(-3, 0)

    def getpipes(self):
        return self.pipes

    def checkCollisions(self, obj):
        for pipe in self.pipes:
            if pipe.pos.colliderect(obj.pos):
                return True
        return False
