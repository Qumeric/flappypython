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
