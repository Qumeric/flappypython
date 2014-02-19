import pygame
from pygame import *
from time import sleep
from random import randrange
from GameObject import *
from PipesController import *

class GameState:
    def __init__(self):
        self.holesize = 50
        self.grav = 0
        self.timer = 0
        self.highscore = 0
    def new(self):
        if self.timer > self.highscore:
            self.highscore = self.timer
        self.holesize = 50
        self.grav = 0
        self.timer = 0

game = GameState()

# Initialize environment
def init_window():
    pygame.init()
    window = display.set_mode((320, 480))
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
    myfont = pygame.font.SysFont("DejaVu Sans", 15)
    pypic = load_image('python.png')
    python = GameObject(pypic, 5, 150, 0, 5)
    pipes = PipesController() 
    screen = pygame.display.get_surface()

    game.new()

    # Handle input and other events
    def eventer(obj):
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN and i.key != K_ESCAPE:
                obj.fly(0, -20)
                game.grav=0
            elif i.type == QUIT or (i.type == KEYDOWN and i.key == K_ESCAPE):
                pygame.quit()
                raise SystemExit

    def endGame(message):
        print(message)
        pipes.clear()
        python.pos.y = 150;
        game.new()

    def checkFall():
        pheight = python.img.get_height()
        if python.pos.y >= 480 - pheight*2:
            endGame('Fail!')
        elif python.pos.y <= 0 + pheight:
            python.pos.y = 0 + pheight;

    while True:
        lScore = myfont.render(str(game.timer), 1, (255,255,0))
        lHighscore = myfont.render(str(game.highscore), 1, (255, 0, 0))

        sleep(0.05)
        game.timer+=1

        draw_background()
        pipes.draw()
        if game.timer%60==0:
            pipes.new(game.holesize)
            game.holesize -= 1


        python.fly(0, game.grav)
        game.grav+=0.2
        

        eventer(python)

        screen.blit(python.img, python.pos)
        

        if pipes.checkCollisions(python):
            pipes.clear()
            endGame('Collision')

        checkFall()

        screen.blit(lScore, (100, 100))
        screen.blit(lHighscore, (100, 120))

        display.flip()

# Self-descriptive
def main():
    init_window()
    draw_background()
    action()

if __name__ == '__main__': main()
