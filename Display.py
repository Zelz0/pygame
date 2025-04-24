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

ground = pygame.Surface((config.GROUND_WIDTH, config.GROUND_HEIGHT))
clock = pygame.time.Clock()

player = Player()
lives = config.STARTING_LIVES
heart_image = pygame.image.load(config.HEART_IMAGE).convert_alpha()
heart_image = pygame.transform.scale(heart_image, (30, 30))  # Size of each heart

running = True
while running:
    game_screen.fill((0, 0, 0))
    ground.fill((80, 140, 250))
    game_screen.blit(ground, (0, 760))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if player.alive:
        player.move(keys)
        player.draw(game_screen)

    for i in range(lives):
        heart_x = config.SCREEN_WIDTH - (i + 1) * 40
        heart_y = 10
        game_screen.blit(heart_image, (heart_x, heart_y))

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
