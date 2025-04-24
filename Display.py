import pygame
import config
from player import Player
import Welcome

pygame.init()
pygame.mixer.init()


game_screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("My Game")
font = pygame.font.SysFont(None, 30)

Welcome.run_welcome_screen(game_screen, font)

print("Game starts here!")

ground = pygame.Surface((config.GROUND_WIDTH, config.GROUND_HEIGHT))
clock = pygame.time.Clock()

player = Player()

surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

#background = pygame.image.load("BackgroundImageFile").convert()

running = True
while running:
    game_screen.fill((0,0,0))
    game_screen.blit(game_screen,(0, 0))
    ground.fill((80,140,250))
    game_screen.blit(ground, (0,760))

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
        player.draw(game_screen)
    pygame.display.flip()
