import pygame
import config

pygame.init()
pygame.mixer.init()

#Hey Andrik! This is the display part I kinda set up but feel free to change/adjust it however you like
#If you want to import an image for the background you can also adjust the width/height of the display in the config.py file to match the background you plan to import.
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

surface = pygame.Surface((config.WIDTH, config.HEIGHT))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(surface,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False