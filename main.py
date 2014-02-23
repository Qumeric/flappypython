from pygame import *
from random import randrange
from GameObject import *

SCORE_COLOR = (255, 255, 0)
HIGHSCORE_COLOR = (255, 0, 0)

DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 480

FONT = None
FONT_SIZE = 22
HOLE_SIZE = 50

PIPE_FREQUENCY = 50
PIPE_MAXLIFETIME = 100

TOP = -50

score = 1
highscore = 0

def save(): 
    global score, highscore
    if score > highscore:
        highscore = score
        with open('save', 'a+') as f:
            f.seek(0)
            save = f.read()
            if highscore > int(save) if save.isdigit() else '0':
                f.seek(0)
                f.truncate()
                f.write(str(highscore))
            else:
                highscore = int(save)
    score = 0

def main():
    global score, highscore
    init()
    window = display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    display.set_caption('Flappy bird')
    myfont = font.Font(FONT, FONT_SIZE)
    screen = display.get_surface()
    bird = Bird(150, 1)
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
        
        # Create new pipes
        if score%PIPE_FREQUENCY==0:
            hole = randrange(HOLE_SIZE, DISPLAY_HEIGHT-HOLE_SIZE) 
            pipepic = image.load('pipe.png').convert_alpha()
            pipes.append(Pipe(DISPLAY_WIDTH, hole+HOLE_SIZE))
            pipes.append(Pipe(DISPLAY_WIDTH, -DISPLAY_HEIGHT+hole-HOLE_SIZE))

        # Move pipes
        for pipe in pipes:
            screen.blit(pipe.img, pipe.rect)
            pipe.fly()

        # Remove old pipes
        for pipe in pipes:
            if pipe.lifetime > PIPE_MAXLIFETIME:
                pipes.remove(pipe)

        bird.fly()

        # Handle the input
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN:
                bird.speedY=-10
            elif i.type == QUIT:
                running = False

        # Check collisions with pipes and bottom
        if bird.rect.y >= DISPLAY_HEIGHT - bird.img.get_height()or bird.checkCollisions(pipes): # The bird is too low or touches a pipe
            bird.die()
            pipes.clear()
            save()
        elif bird.rect.y < TOP: # The bird is too high
            bird.speedY = 1

        # Draw the bird and score info
        screen.blit(bird.img, bird.rect)
        screen.blit(lScore, (0, 0))
        screen.blit(lHighscore, (0, FONT_SIZE))

        display.flip()

if __name__ == '__main__': main()
