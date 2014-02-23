from pygame import image

MAX_SPEED = 15

class Bird():
    def __init__(self, y, gravity):
        self.img = image.load('bird.png').convert_alpha()
        self.speedY = 0 
        self.rect = self.img.get_rect().move(0, y)
        self.oldY = y
        self.gravity = gravity

    def fly(self):
        self.rect = self.rect.move(0, self.speedY)
        if not abs(self.speedY) > MAX_SPEED:
            self.speedY+=self.gravity

    def die(self):
        self.rect.y = self.oldY
        self.speedY = 0

    def checkCollisions(self, pipes):
        for pipe in pipes:
            if self.rect.colliderect(pipe.rect):
                return True
        return False

class Pipe():
    def __init__(self, x, y):
        self.img = image.load('pipe.png').convert_alpha()
        self.rect = self.img.get_rect().move(x, y)
        self.lifetime = 0

    def fly(self):
        self.rect = self.rect.move(-5, 0)
        self.lifetime += 1
