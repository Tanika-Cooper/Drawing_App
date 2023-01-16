import sys
import pygame
from ButtonClass import Button

def myFunction():
    print('Button Pressed')


# Config
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

customButton = Button(30, 30, 400, 100, screen, 'Button One', myFunction)

# Game Loop
while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for button in customButton.objects:
        button.process()

    pygame.display.flip()
    fpsClock.tick(fps)