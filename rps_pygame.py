import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rock Paper Scissors')

def play_round():
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Play a new round if the user pressed the space bar
            if event.key == K_SPACE:
                play_round()
            # Quit if the user pressed the escape key
            if event.key == K_ESCAPE:
                running = False
        # Quit of the user closed the window
        elif event.type == QUIT:
            running = False