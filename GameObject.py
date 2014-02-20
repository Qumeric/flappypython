class GameObject:
    def __init__(self, img, x, y, speedX=0, speedY=0, gravity=0):
        self.img = img
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.pos = img.get_rect().move(x, y)
        self.gravity = gravity
    def fly(self):
        self.pos = self.pos.move(self.speedX, self.speedY)
        self.speedY+=self.gravity

