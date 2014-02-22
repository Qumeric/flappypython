from pygame import *
from random import randrange
from GameObject import *

SCORE_COLOR = (255, 255, 0)
HIGHSCORE_COLOR = (255, 0, 0)
DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 480
FONT = None
FONT_SIZE = 22

score = 1
highscore = 0

def save(): 
    global score, highscore
    if score > highscore:
        highscore = score
        try:
            with open('save', 'r+') as f:
                save = f.read()
                if highscore > int(save):
                    f.seek(0)
                    f.truncate()
                    f.write(str(highscore))
                else:
                    highscore = int(save)
        except:
            print('Save must be corrupted. Set highscore to 0 :(')
            f = open('save', 'w')
            f.write('0')
            f.close()
    score = 0

# Main game cycle
def main():
    global score, highscore
    pygame.init()
    window = display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    display.set_caption('Flappy bird')
    myfont = font.Font(FONT, FONT_SIZE)
    screen = display.get_surface()
    bird = GameObject(image.load('bird.png').convert_alpha(), 5, 150, gravity=1)
    bg = image.load('background.png').convert_alpha()
    pipes = []

    save()

    running = True
    while running:
        lScore     = myfont.render(str(score),     True, SCORE_COLOR)
        lHighscore = myfont.render(str(highscore), True, HIGHSCORE_COLOR)

        time.Clock().tick(30)
        screen.blit(bg, (0, 0))
        score+=1

        for pipe in pipes:
            if pipe.pos.x <= -pipe.img.get_width():
                pipes.remove(pipe)
            else:
                pipe.fly()
                screen.blit(pipe.img, pipe.pos)

        if score%60==0:
            hole = randrange(0, 480) 
            pipepic = image.load('pipe.png').convert_alpha()
            pipes.append(GameObject(pipepic, 240, hole+50, -5, 0))
            pipes.append(GameObject(pipepic, 240, -480+hole-50, -5, 0))

        bird.fly()

        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN and i.key != K_ESCAPE:
                bird.speedY=-10
            elif i.type == QUIT or (i.type == KEYDOWN and i.key == K_ESCAPE):
                running = False

        screen.blit(bird.img, bird.pos)

        pheight = bird.img.get_height()
        if bird.pos.y >= 480 - pheight*1.5 or bird.checkCollisions(pipes):
            bird.die()
            pipes.clear()
            save()
        elif bird.pos.y <= pheight/2:
            bird.pos.y = pheight/2;
            bird.speedY = 1

        screen.blit(lScore, (100, 100))
        screen.blit(lHighscore, (100, 120))

        display.flip()

if __name__ == '__main__': main()
