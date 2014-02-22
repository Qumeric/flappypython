import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speedX=0, speedY=0, gravity=0, maxspeed=15):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.oldX = x
        self.oldY = y
        self.speedX = speedX
        self.speedY = speedY
        self.pos = img.get_rect().move(x, y)
        self.gravity = gravity
        self.maxspeed = maxspeed
    def fly(self):
        self.pos = self.pos.move(self.speedX, self.speedY)
        if not self.speedY > self.maxspeed:
            self.speedY+=self.gravity
    def die(self):
        self.pos.x = self.oldX
        self.pos.y = self.oldY
        self.speedX = self.speedY = 0
    def checkCollisions(self, pipes):
        for pipe in pipes:
            if self.pos.colliderect(pipe.pos):
                return True
        return False
