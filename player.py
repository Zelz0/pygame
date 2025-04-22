import pygame
import config

#There's a # in front of some lines so we can update them with the correct image file, then remove the #
class Player:
    def __init__(self):
        self.speed = config.PLAYER_SPEED
        self.sprite = pygame.image.load(config.PLAYER_IMAGE).convert_alpha()
        self.rect = self.sprite.get_rect(center=(config.WIDTH // 2, config.HEIGHT - 50))
        self.alive = True
        #self.dead_sound = pygame.mixer.Sound(config.PLAYER_DEAD_SOUND)

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < config.WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
