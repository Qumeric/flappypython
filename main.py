from pygame import display, font, image, init, time, event
from pygame.locals import *
from random import randrange
from GameObject import Bird, Pipe

SCORE_COLOR = (255, 255, 0)
HIGHSCORE_COLOR = (255, 165, 0)

DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 480

FONT = None
FONT_SIZE = 22
HOLE_SIZE = 50

PIPE_FREQUENCY = 50
PIPE_MAXLIFETIME = 100

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


def pause(display):
    screen = display.get_surface()

    hsfont = font.Font(FONT, 100)
    hs = hsfont.render(str(highscore), True, HIGHSCORE_COLOR)

    screen.blit(image.load('pause.png').convert_alpha(), (0, 0))
    screen.blit(hs, (77, 110))
    display.flip()

    while True:
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN:
                    return


def main():
    global score, highscore
    init()
    display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    display.set_caption('Flappy bird')
    myfont = font.Font(FONT, FONT_SIZE)
    screen = display.get_surface()
    bird = Bird(150, 1)
    bg = image.load('background.png').convert_alpha()
    pipes = []

    save()

    running = True

    while running:
        lScore = myfont.render(str(score), True, SCORE_COLOR)

        time.Clock().tick(30)  # Set FPS to 30
        screen.blit(bg, (0, 0))
        score += 1

        # Create new pipes
        if score % PIPE_FREQUENCY == 0:
            hole = randrange(HOLE_SIZE, DISPLAY_HEIGHT - HOLE_SIZE)
            pipe1 = Pipe(DISPLAY_WIDTH, hole + HOLE_SIZE)
            pipe2 = Pipe(DISPLAY_WIDTH, -DISPLAY_HEIGHT + hole - HOLE_SIZE)
            pipes.extend((pipe1, pipe2))

        # Move pipes
        for pipe in pipes:
            screen.blit(pipe.img, pipe.rect)
            pipe.fly()

        # Remove old pipes
        for pipe in pipes:
            if pipe.lifetime > PIPE_MAXLIFETIME:
                pipes.remove(pipe)

        # Move the bird on the y-axis
        bird.fly()

        # Handle the input
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN or i.type == KEYDOWN:
                bird.speedY = -10
            elif i.type == QUIT:
                running = False

        # Check collisions with pipes and bottom
        # If the bird is too low or touches a pipe
        if bird.rect.y >= DISPLAY_HEIGHT - bird.img.get_height() or \
                bird.checkCollisions(pipes):
            bird.die()
            pipes.clear()
            save()
            pause(display)
        elif bird.rect.y < -HOLE_SIZE:  # The bird is too high
            bird.speedY = 1

        # Draw the bird and score info
        screen.blit(bird.img, bird.rect)
        screen.blit(lScore, (0, 0))

        display.flip()

if __name__ == '__main__':
    main()
