import pygame
from pygame import *
from time import sleep
from random import randrange
from GameObject import *
from PipesController import *

# Initialize environment
def init_window():
    pygame.init()
    window = display.set_mode((480, 320))
    display.set_caption('Flappy python')

# Macros for pygame.image.load(name)
def load_image(name):
    try:
        image = pygame.image.load(name).convert_alpha()
    except pygame.error:
        print('Cannot load image:', name)
        raise SystemExit
    return image

# Draw background :)
def draw_background():
    screen = pygame.display.get_surface()
    background = load_image('background.png')
    background_rect  = background.get_rect()
    screen.blit(background, (0, 0))
    pygame.display.flip()
    return background

# Main game cycle
def action():
    pypic = load_image('python.png')
    python = GameObject(pypic, 5, 150, 0, 5)
    pipes = PipesController() 
    screen = pygame.display.get_surface()

    # Handle input and other events
    def eventer(obj):
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN:
                obj.fly(0, -20)

    def endGame(message):
        print(message)
        pipes.clear()
        python.pos.y = 150;

    def checkFall():
        pheight = python.img.get_height()
        if python.pos.y >= 360 - pheight*2:
            endGame('Fail!')
        elif python.pos.y <= 0 + pheight:
            python.pos.y = 0 + pheight;

    while True:
        sleep(0.1)
        draw_background()
        pipes.new()

        python.fly(0, 1)

        eventer(python)

        screen.blit(python.img, python.pos)
        
        pipes.draw()

        if pipes.checkCollisions(python):
            pipes.clear()
            endGame('Collision')

        display.flip()

# Self-descriptive
def main():
    init_window()
    draw_background()
    action()

if __name__ == '__main__': main()
