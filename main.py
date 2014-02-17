from pygame import *
from time import sleep
import sys

init()

screen = display.set_mode((480, 320))

display.set_caption('Flappy python')

background = image.load('background.png')

screen.blit(background, (0, 0))

class Python:
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
python = Python(pypic, 160, 240, 0, 5)    # FIXME

timer = 0
pipes = []

while True:
    timer += 1
    sleep(0.03)
    if timer%100==0:
        pipes.append(1) # FIXME
    screen.blit(background, (0, 0));
    python.fly(0, 1)
    for i in event.get():
        python.fly(0, -20)
    screen.blit(python.img, python.pos)

    display.flip()
