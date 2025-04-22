import pygame
import config
from player import Player

pygame.init()
pygame.mixer.init()

#There's a # in front of some lines so we can update them with the correct image file, then remove the #

#Hey Andrik! This is the display part I kinda set up but feel free to change/adjust it however you like
#If you want to import an image for the background you can also adjust the width/height of the display in the config.py file to match the background you plan to import.
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
ground = pygame.Surface((config.GROUND_WIDTH, config.GROUND_HEIGHT))
clock = pygame.time.Clock()

player = Player()

surface = pygame.Surface((config.WIDTH, config.HEIGHT))

#background = pygame.image.load("BackgroundImageFile").convert()

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(screen,(0, 0))
    ground.fill((80,140,250))
    screen.blit(ground, (0,760))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if player.alive:
        player.move(keys)

    if player.alive:
        player.draw(screen)
    pygame.display.flip()
