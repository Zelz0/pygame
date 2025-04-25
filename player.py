import pygame
import config

class Player:
    def __init__(self):
        self.image = pygame.image.load("img/ShoppingCart.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.speed = config.PLAYER_SPEED
        self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT-70))
        self.alive = True
        self.dead_sound = pygame.mixer.Sound(config.SOUND_GAME_OVER)

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < config.SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, game_screen):
        game_screen.blit(self.image, self.rect)
