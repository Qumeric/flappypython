import pygame
from GameObject import GameObject
from random import randrange

class PipesController():
    def __init__(self):
        self.pipes = []
    
    def clear(self):
        del self.pipes[:]
    
    def new(self, size):
        hole = randrange(size*2, 480 - size*2)
        pipepic = pygame.image.load('pipe.png').convert_alpha()
        pipe1 = GameObject(pipepic, 240, hole+size, -5, 0)
        pipe2 = GameObject(pipepic, 240, -480+hole-size, -5, 0)
        self.pipes.append(pipe1)
        self.pipes.append(pipe2)


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
