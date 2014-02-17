from pygame import *
from time import sleep
from random import randrange
import sys

init()

screen = display.set_mode((480, 320))

display.set_caption('Flappy python')

background = image.load('background.png')

screen.blit(background, (0, 0))

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
pipes = []

while True:
    timer += 1
    sleep(0.03)
    if timer%100==0:
        pipepic = image.load('pipe.png')
        pipe = GameObject(pipepic, 100, randrange(0, 240), -5, 0)
        pipes.append(pipe)
        if pipes[0].x <= 0:
            pipes.pop(0)
    screen.blit(background, (0, 0));
    python.fly(0, 1)
    for i in event.get():
        python.fly(0, -20)
    screen.blit(python.img, python.pos)
    for i in pipes:
        screen.blit(i.img, i.pos)
        i.fly(-3, 0)

    display.flip()
