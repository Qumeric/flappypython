from pygame import *
from time import sleep
from random import randrange
import sys

init()

screen = display.set_mode((480, 320))

display.set_caption('Flappy python')

background = image.load('background.png')

screen.blit(background, (0, 0))

myfont = font.SysFont("DejaVu Sans", 18)

class GameObject:
    def __init__(self, img, x, y, speedX, speedY):
        self.img = img
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.pos = img.get_rect().move(x, y)
    def fly(self, sX, sY):
        self.pos = self.pos.move(sX, sY)

pypic = image.load('python.png')
python = GameObject(pypic, 5, 240, 0, 5)    # FIXME

timer = 0
highscore = 0
pipes = []

while True:
    timer += 1
    sleep(0.03)
    if timer%100==0:
        pipepic = image.load('pipe.png')
        pipe = GameObject(pipepic, 240, randrange(0, 240), -5, 0)
        pipes.append(pipe)
        if len(pipes) >= 5:
            pipes.pop(0)

    screen.blit(background, (0, 0));
    python.fly(0, 1)
    for i in event.get():
        if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN:
            python.fly(0, -20)
    screen.blit(python.img, python.pos)
    for i in pipes:
        screen.blit(i.img, i.pos)
        i.fly(-3, 0)
        if i.pos.colliderect(python.pos) or python.y <= 0 :
            print("Collide!")
            highscore = timer
            timer = 0
            pipes = []

    hslabel = myfont.render(str(highscore), 1, (0, 255, 0))
    screen.blit(hslabel, (100, 70))
    label = myfont.render(str(timer), 1, (0, 0, 255))
    screen.blit(label, (100, 100))
    # DEBUG: print(pipes)

    display.flip()
